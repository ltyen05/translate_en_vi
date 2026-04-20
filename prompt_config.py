import chromadb
from chromadb.utils import embedding_functions
import re
import unicodedata
from sentence_transformers import CrossEncoder

# 1. System Prompt Template
system_prompt = """Bạn là một hệ thống dịch đa ngôn ngữ cấp chuyên gia, được tối ưu cho dịch theo ngữ cảnh (context-aware) và theo lĩnh vực (domain-aware) sử dụng Retrieval-Augmented Generation (RAG).

---

## MỤC TIÊU

Dịch văn bản đầu vào một cách chính xác, đảm bảo:
* Đúng thuật ngữ chuyên ngành
* Phù hợp ngữ cảnh
* Tự nhiên trong ngôn ngữ đích

---

## CẤU TRÚC ĐẦU VÀO

Bạn sẽ nhận được các thông tin sau:
* Lĩnh vực: {domain}
* Từ điển thuật ngữ: {terminology}
* Ngữ cảnh truy xuất (RAG): {context}
* Văn bản nguồn: {source_text}
* Ngôn ngữ nguồn: {source_lang}
* Ngôn ngữ đích: {target_lang}

---

## NGUYÊN TẮC CỐT LÕI

### 1. ƯU TIÊN LĨNH VỰC (CAO NHẤT)
* Luôn ưu tiên nghĩa theo lĩnh vực hơn nghĩa thông thường
* Nếu một thuật ngữ có trong từ điển → BẮT BUỘC dùng chính xác
* Không được đơn giản hóa hoặc thay đổi thuật ngữ chuyên ngành

---

### 2. TUÂN THỦ THUẬT NGỮ
* Phải sử dụng đúng từ điển thuật ngữ đã cung cấp
* Nếu có nhiều nghĩa:
  1. Ưu tiên theo lĩnh vực
  2. Sau đó theo ngữ cảnh
  3. Cuối cùng mới đến nghĩa phổ thông
* Không tự tạo thuật ngữ mới

---

### 3. SỬ DỤNG NGỮ CẢNH (RAG)
* Dùng {context} để:
  * Làm rõ nghĩa
  * Đảm bảo tính nhất quán
* Nếu ngữ cảnh mâu thuẫn với kiến thức chung → ưu tiên ngữ cảnh

---

### 4. CHẤT LƯỢNG BẢN DỊCH
* Bản dịch phải:
  * Đúng nghĩa
  * Tự nhiên, trôi chảy
  * Đúng ngữ pháp
* Giữ nguyên tone (technical / formal / neutral)

---

### 5. GIỮ NGUYÊN CẤU TRÚC
* Bảo toàn:
  * Format (markdown, bullet, code…)
  * Số, đơn vị, ký hiệu
* Không thay đổi cấu trúc trừ khi cần thiết

---

### 6. XỬ LÝ MƠ HỒ
Nếu câu hoặc từ mơ hồ:
* Ưu tiên dùng context
* Sau đó dùng domain
* Nếu vẫn chưa rõ:
  * Chọn nghĩa hợp lý nhất theo lĩnh vực
  * Không hỏi lại
  * Không suy diễn thêm

---

### 7. NGĂN NGỪA LỖI
KHÔNG được:
* Bịa nội dung
* Thêm giải thích
* Dịch từng từ nếu làm sai nghĩa
* Bỏ qua cách diễn đạt chuyên ngành

---

### 8. CHIẾN LƯỢC FALLBACK
* Thiếu terminology → suy luận theo domain + context
* Thiếu context → dựa vào domain
* Thiếu cả hai → dịch trung tính nhưng chính xác

---

### 9. RÀNG BUỘC OUTPUT
* Chỉ trả về bản dịch
* Không giải thích
* Không thêm tiền tố như "Bản dịch:"

---

## GỢI Ý LĨNH VỰC (DEFAULT)

* IT: ưu tiên chính xác kỹ thuật (API, model, pipeline…)
* Y tế: ưu tiên chính xác lâm sàng
* Pháp lý: ưu tiên formal và chặt chẽ

---

## KIỂM TRA CUỐI

* Đúng thuật ngữ?
* Đúng ngữ cảnh?
* Đúng lĩnh vực?
* Tự nhiên?

Nếu đạt tất cả → xuất bản dịch.
"""

# 2. Khởi tạo ChromaDB
local_ef = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path="./VectorDB_Gemini")
collection = client.get_or_create_collection(
    name="multi_domain_rag_kb",
    embedding_function=local_ef
)

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
    Sử dụng tìm kiếm đa tầng và xếp hạng lại (Reranking).
    """
    # 0. Chuẩn bị đầu vào
    user_input_norm = normalize_text(user_input)
    # Trích xuất từ khóa để tìm Glossary chính xác hơn
    keywords = [w for w in re.split(r'\W+', user_input) if len(w) > 3]
    
    domains_to_search = []
    if domain:
        if "_" in domain:
            domains_to_search = [domain]
        else:
            domains_to_search = [f"{domain}_glossary", f"{domain}_context"]
    
    # 1. Truy xuất đa tầng (Multi-Query Retrieval)
    # 1.1 Tìm Glossary
    gloss_where = {"domain": {"$in": [d for d in domains_to_search if "glossary" in d]}} if domains_to_search else {"domain": {"$ne": ""}}
    gloss_queries = [user_input] + keywords[:5]
    gloss_results = collection.query(query_texts=gloss_queries, n_results=15, where=gloss_where)

    # 1.2 Tìm Context
    ctx_where = {"domain": {"$in": [d for d in domains_to_search if "context" in d]}} if domains_to_search else None
    ctx_results = collection.query(query_texts=[user_input], n_results=30, where=ctx_where)

    # Gộp kết quả và lọc trùng
    all_docs = []
    all_metas = []
    seen_ids = set()

    for r in [gloss_results, ctx_results]:
        if r.get("documents"):
            for i in range(len(r["documents"])):
                for j in range(len(r["documents"][i])):
                    doc_id = r["ids"][i][j]
                    if doc_id not in seen_ids:
                        all_docs.append(r["documents"][i][j])
                        all_metas.append(r["metadatas"][i][j])
                        seen_ids.add(doc_id)

    if not all_docs:
        return "Không có ngữ cảnh bổ trợ đặc biệt nào được tìm thấy."

    # 2. Xếp hạng lại (Reranking)
    hits = [[user_input, doc] for doc in all_docs]
    scores = reranker.predict(hits)
    
    reranked = []
    for i in range(len(all_docs)):
        reranked.append({
            "text": all_docs[i],
            "metadata": all_metas[i],
            "score": scores[i]
        })
    # Sắp xếp theo điểm số giảm dần
    reranked.sort(key=lambda x: x["score"], reverse=True)
    top_results = reranked[:15] # Lấy top 15 sau khi xếp hạng

    # 3. Phân loại và tạo prompt
    tm_context = "[NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]\n"
    glossary_context = "[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]\n"
    found_tm = False
    found_glos = False
    
    # Tập hợp tất cả ứng viên (không chỉ top 15) để tìm glossary chắc chắn hơn
    # Glossary thường có điểm semantic thấp hơn câu dài nhưng độ chính xác khớp từ lại cao
    all_candidates = []
    seen_texts = set()
    for item in reranked:
        if item["text"] not in seen_texts:
            all_candidates.append(item)
            seen_texts.add(item["text"])

    # Xử lý Glossary trước trên toàn bộ ứng viên
    for item in all_candidates:
        text = item["text"]
        meta = item["metadata"]
        item_domain = str(meta.get("domain", "General"))
        vi = meta.get("vi", "N/A")

        is_glossary = "glossary" in item_domain.lower() or len(text.split()) <= 5
        
        if is_glossary:
            text_norm = normalize_text(text)
            # Hỗ trợ cả trường hợp "meniere s" và "meniere"
            pattern = r'\b' + re.escape(text_norm).replace('\ s', '\ ?s?') + r"(?: s)?\b"
            if re.search(pattern, user_input_norm):
                # Chỉ thêm nếu chưa có trong glossary_context
                term_entry = f"- '{text}': {vi} (Lĩnh vực: {item_domain})\n"
                if term_entry not in glossary_context:
                    glossary_context += term_entry
                    found_glos = True

    # Xử lý Context chỉ lấy Top 10 thực sự chất lượng
    for item in reranked[:10]:
        text = item["text"]
        meta = item["metadata"]
        item_domain = str(meta.get("domain", "General"))
        vi = meta.get("vi", "N/A")

        is_glossary = "glossary" in item_domain.lower() or len(text.split()) <= 5
        if not is_glossary:
            tm_context += f"- Tiếng Anh: {text}\n  Nghĩa: {vi}\n"
            found_tm = True

    final_prompt = ""
    if found_tm: final_prompt += tm_context + "\n"
    if found_glos: final_prompt += glossary_context
    
    return final_prompt if final_prompt else "Không tìm thấy thuật ngữ hay ngữ cảnh cụ thể."

def format_qwen_prompt(user_input, context, domain="Đa lĩnh vực", terminology="Xem danh sách bên dưới", source_lang="English", target_lang="Vietnamese"):
    """Định dạng prompt ChatML cho Qwen."""
    system_content = system_prompt.format(
        domain=domain,
        terminology=terminology,
        context=context,
        source_text=user_input,
        source_lang=source_lang,
        target_lang=target_lang
    )
    return f"<|im_start|>system\n{system_content}<|im_end|>\n<|im_start|>user\nDịch câu này: {user_input}<|im_end|>\n<|im_start|>assistant\n"