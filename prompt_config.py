import chromadb
from chromadb.utils import embedding_functions
import re
import unicodedata
from sentence_transformers import CrossEncoder

# 1. System Prompt Template (Tối ưu hóa: Loại bỏ lặp lại văn bản nguồn)
system_prompt = """Bạn là hệ thống dịch thuật chuyên nghiệp (RAG-based Machine Translation System).

NHIỆM VỤ CHÍNH:
- Dịch chính xác từ {source_lang} sang {target_lang}
- Chỉ trả về một bản dịch cuối cùng duy nhất

---

## DỮ LIỆU ĐẦU VÀO:
- Domain: {domain}
- Glossary (thuật ngữ bắt buộc): {terminology}
- Context (ngữ cảnh đoạn văn): {context}
- (Optional) Few-shot examples: {examples}

---

## QUY TẮC TUYỆT ĐỐI:
1. KHÔNG giải thích dưới bất kỳ hình thức nào
2. KHÔNG trả lời nhiều phương án
3. KHÔNG paraphrase hoặc mở rộng ý nghĩa
4. KHÔNG lặp lại input
5. KHÔNG thêm thông tin ngoài nội dung gốc
6. Luôn ưu tiên nghĩa phù hợp nhất với context + domain
7. Giữ nguyên:
   - tên riêng
   - số liệu
   - ngày tháng
   - ký hiệu kỹ thuật
8. Nếu có nhiều nghĩa:
   - CHỈ chọn 1 nghĩa đúng nhất theo context
9. Nếu là câu hỏi:
   - giữ nguyên cấu trúc câu hỏi và dấu "?"

---

## DOMAIN AWARENESS:
- Luôn ưu tiên cách dịch đúng theo domain đã cung cấp
- Nếu glossary có thuật ngữ → bắt buộc dùng đúng thuật ngữ đó
- Không tự ý thay đổi thuật ngữ đã định nghĩa

---

## FEW-SHOT LEARNING (QUAN TRỌNG):
Nếu có examples:
- Học theo pattern của examples
- Ưu tiên similarity về:
  - ngữ nghĩa
  - cấu trúc câu
  - domain
- Không copy máy móc, nhưng phải giữ phong cách tương tự

---

## CONTEXT CONSISTENCY:
- Nếu cùng một thuật ngữ xuất hiện nhiều lần:
  → phải dịch nhất quán trong toàn bộ đoạn
- Không được thay đổi cách dịch giữa chừng

---

## OUTPUT CONSTRAINT (CỰC KỲ QUAN TRỌNG):
- Chỉ trả về 1 dòng duy nhất
- Chỉ chứa bản dịch cuối cùng
- KHÔNG markdown
- KHÔNG ngoặc
- KHÔNG nhãn
- KHÔNG giải thích
- KHÔNG thêm ký tự thừa

---

## FAILURE POLICY:
- Nếu input mơ hồ → chọn nghĩa hợp lý nhất theo context
- KHÔNG được hỏi lại người dùng
- KHÔNG được trả nhiều phương án

---

## QUALITY TARGET:
Bản dịch phải đạt mức:
- như dịch giả chuyên nghiệp bản ngữ
- đúng ngữ nghĩa 100%
- tự nhiên trong ngôn ngữ đích
"""
# 2. Khởi tạo ChromaDB
local_ef = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path="./VectorDB_Gemini")

# 3. Khởi tạo Reranker
print("Loading Reranker model (ms-marco-MiniLM-L-6-v2) for multi-stage RAG...")
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def normalize_text(text: str) -> str:
    """Loại bỏ dấu (accents) và chuẩn hóa ký tự để so khớp linh hoạt."""
    if not text: return ""
    text = unicodedata.normalize('NFD', text.lower())
    text = ''.join([c for c in text if unicodedata.category(c) != 'Mn'])
    text = unicodedata.normalize('NFC', text)
    # Thay ký tự đặc biệt bằng dấu cách
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    return ' '.join(text.split())

def get_context_prompt(user_input, domain=None):
    """
    Truy xuất ngữ cảnh và thuật ngữ từ cơ sở tri thức (RAG).
    Sử dụng tìm kiếm đa tầng, Threshold Reranker Bypass và xếp hạng lại.
    """
    # 0. Chuẩn bị đầu vào
    user_input_norm = normalize_text(user_input)
    
    # --- DYNAMIC CONTEXT RETRIEVAL ---
    word_count = len(user_input.split())
    if word_count < 30:
        query_n_results = 5
        max_context = 2
    elif word_count <= 100:
        query_n_results = 10
        max_context = 5
    else:
        query_n_results = 15
        max_context = 8
        
    keywords = [w for w in re.split(r'\W+', user_input) if len(w) > 3]
    
    # --- DOMAIN ROUTING DỰA VÀO ĐẦU VÀO ---
    target_collections = ["general_kb"] # Luôn kèm general fallback
    if domain:

        if "medical" in domain.lower() or "y tế" in domain.lower(): target_collections.insert(0, "medical_kb")
        elif "economic" in domain.lower() or "kinh tế" in domain.lower(): target_collections.insert(0, "economic_kb")
        elif "technical" in domain.lower() or "công nghệ" in domain.lower(): target_collections.insert(0, "technical_kb")
        else: 
            # Nếu domain truyền vào không khớp 3 cái trên, quét tất cả
            target_collections = ["medical_kb", "economic_kb", "technical_kb", "general_kb"]

    # 1. Truy xuất ChromaDB
    all_docs = []
    all_metas = []
    all_distances = []
    seen_ids = set()
    seen_glossary = set()
    # Gộp từ khóa thành 1 chuỗi để giảm số lượng query
    keyword_str = " ".join(keywords[:5])
    queries = [user_input]
    if keyword_str: 
        queries.append(keyword_str)

    for col_name in target_collections:
        try:
            col = client.get_collection(name=col_name, embedding_function=local_ef)
        except Exception:
            continue
            
        results = col.query(query_texts=queries, n_results=query_n_results)

        if results.get("documents"):
            for i in range(len(results["documents"])):
                for j in range(len(results["documents"][i])):
                    doc_id = results["ids"][i][j]
                    if doc_id not in seen_ids:
                        all_docs.append(results["documents"][i][j])
                        all_metas.append(results["metadatas"][i][j])
                        all_distances.append(results["distances"][i][j])
                        seen_ids.add(doc_id)

    if not all_docs:
        return "Không có ngữ cảnh bổ trợ đặc biệt nào được tìm thấy."

    # 2. Tiền xử lý Reranking / Bypass Reranker
    pre_filtered = list(zip(all_docs, all_metas, all_distances))
    pre_filtered.sort(key=lambda x: x[2]) # Sắp xếp theo L2 Distance (nhỏ nhất = tốt nhất)
    top_candidates = pre_filtered[:25] # Cắt top 25
    
    reranked = []
    
    # ChromaDB dùng All-MiniLM-L6-v2 (L2 distance). 
    # Nếu distance < 0.6 => Cosine Similarity > 0.7. Distance < 0.4 => Similarity > 0.8
    BYPASS_DISTANCE_THRESHOLD = 0.5 
    
    # Kiểm tra xem top 5 candidates đầu tiên có đủ tốt để bypass reranker không
    is_bypass = False
    if len(top_candidates) > 0:
        top_5_distances = [dist for _, _, dist in top_candidates[:5]]
        # Nếu trung bình khoảng cách top 5 < Threshold, thì bypass Reranker
        if sum(top_5_distances) / len(top_5_distances) <= BYPASS_DISTANCE_THRESHOLD:
            is_bypass = True

    if is_bypass:
        print("⚡ Bypassing Reranker (Vector Search confidence is high: >80%)")
        for doc, meta, dist in top_candidates:
            reranked.append({
                "text": doc,
                "metadata": meta,
                "score": 1.0 - (dist / 2.0), # Quy đổi distance ra fake score để tái sử dụng code cũ
                "is_bypass": True
            })
    else:
        # Nếu chưa đủ tự tin, chạy CrossEncoder
        hits = [[user_input, doc] for doc, meta, dist in top_candidates]
        scores = reranker.predict(hits)
        for i in range(len(top_candidates)):
            doc, meta, dist = top_candidates[i]
            reranked.append({
                "text": doc,
                "metadata": meta,
                "score": scores[i],
                "is_bypass": False
            })
        # Sắp xếp lại theo điểm số Reranker giảm dần
        reranked.sort(key=lambda x: x["score"], reverse=True)

    # 3. Phân loại và tạo prompt
    tm_context = "[NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]\n"
    glossary_context = "[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]\n"
    found_tm = False
    found_glos = False
    
    # Nếu chạy CrossEncoder, threshold = 0.5. Nếu bypass (fake score), threshold = 0.75 (ứng với distance 0.5)
    seen_texts = set()

    # Xử lý Glossary
    for item in reranked:
        text = item["text"]
        meta = item["metadata"]
        score = item["score"]
        is_bypass = item["is_bypass"]
        
        item_domain = str(meta.get("domain", "General"))
        vi = meta.get("vietnamese", "N/A")

        is_glossary = (
            "glossary" in item_domain.lower()
            and len(text.split()) <= 4
        )
        
        # Threshold lọc rác
        threshold_met = (is_bypass and score >= 0.7) or (not is_bypass and score >= 0.5)
        
        if is_glossary and threshold_met:
            text_norm = normalize_text(text)
            pattern = r'\b' + re.escape(text_norm).replace('\\ ', ' ?s?') + r"(?: s)?\b"
            if re.search(pattern, user_input_norm):
                term_entry = f"- {text} => {vi}\n"
                if term_entry not in glossary_context:
                    glossary_context += term_entry
                    found_glos = True
                    seen_texts.add(text)

    # Xử lý Context (Dynamic: max_context)
    context_count = 0
    for item in reranked:
        if context_count >= max_context: break
        text = item["text"]
        if text in seen_texts: continue
        if text in seen_glossary: continue
        seen_glossary.add(text)

        meta = item["metadata"]
        item_domain = str(meta.get("domain", "General"))
        vi = meta.get("vi", "N/A")

        is_glossary = "glossary" in item_domain.lower() or len(text.split()) <= 5
        if not is_glossary:
            tm_context += f"- Tiếng Anh: {text}\n  Nghĩa: {vi}\n"
            found_tm = True
            context_count += 1
            seen_texts.add(text)

    final_prompt = ""
    if found_tm: final_prompt += tm_context + "\n"
    if found_glos: final_prompt += glossary_context
    
    return final_prompt if final_prompt else "Không tìm thấy thuật ngữ hay ngữ cảnh cụ thể."

def format_qwen_prompt(user_input, context, domain="Đa lĩnh vực", terminology="Xem danh sách bên dưới", source_lang="English", target_lang="Vietnamese"):
    """Định dạng prompt ChatML cho Qwen (Đã tối ưu token)."""
    system_content = system_prompt.format(
        domain=domain,
        terminology=terminology,
        context=context,
        source_lang=source_lang,
        target_lang=target_lang
    )
    return f"<|im_start|>system\n{system_content}<|im_end|>\n<|im_start|>user\nDịch đoạn văn này: {user_input}<|im_end|>\n<|im_start|>assistant\n"

def check_semantic_cache(user_input, threshold=0.95):
    """
    Kiểm tra xem đã từng dịch câu này chưa (Sử dụng chính ChromaDB để cache).
    """
    try:
        col = client.get_collection(name="translation_cache", embedding_function=local_ef)
        results = col.query(query_texts=[user_input], n_results=1)
        if results["distances"] and results["distances"][0] and results["distances"][0][0] < (1 - threshold):
            return results["metadatas"][0][0]["translation"]
    except Exception:
        pass
    return None

def add_to_cache(user_input, translation):
    """Lưu bản dịch vào cache."""
    try:
        col = client.get_or_create_collection(name="translation_cache", embedding_function=local_ef)
        import uuid
        col.add(
            ids=[str(uuid.uuid4())],
            documents=[user_input],
            metadatas=[{"translation": translation}]
        )
    except Exception as e:
        print(f"⚠️ Không thể lưu cache: {e}")