import chromadb
from chromadb.utils import embedding_functions
import re
import unicodedata
from sentence_transformers import CrossEncoder
from rapidfuzz import fuzz
from nltk.stem import WordNetLemmatizer

# -------------------------------------------------
# GLOBAL FORCED TRANSLATIONS (domain -> {english: vietnamese})
# -------------------------------------------------

# 1. System Prompt Template
system_prompt = """Bạn là hệ thống dịch thuật chuyên nghiệp (RAG-based Machine Translation System).

NHIỆM VỤ CHÍNH:
- Dịch chính xác từ {source_lang} sang {target_lang}
- Chỉ trả về một bản dịch cuối cùng duy nhất

---

## DỮ LIỆU ĐẦU VÀO:
- Domain: {domain}
- Glossary (thuật ngữ bắt buộc): {terminology}
- Context (ngữ cảnh đoạn văn): {context}

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
- Nếu có cụm từ thì dịch theo cụm từ
- KHÔNG được trả nhiều phương án

---
## SINGLE SENSE RESOLUTION (QUAN TRỌNG NHẤT):
- Cách chọn nghĩa:
  1. Ưu tiên Nghĩa trong Glossary (nếu khớp 100%).
  2. Ưu tiên Nghĩa theo Domain
  3. Ưu tiên Nghĩa PHỔ BIẾN NHẤT trong đời sống (Common Sense). 
   - Tuyệt đối không chọn nghĩa hiếm gặp, nghĩa bóng hoặc nghĩa chuyên ngành nếu đoạn văn thuộc domain 'General'.
   - Ví dụ: Với các cụm từ đa nghĩa, luôn chọn nghĩa mà 90% người bản ngữ sẽ dùng trong ngữ cảnh thông thường.
- TUYỆT ĐỐI CẤM:
  - liệt kê nhiều nghĩa
  - dùng từ “hoặc”, “có thể là”
  - giải thích lựa chọn
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

# 4. Lemmatizer
lemmatizer = WordNetLemmatizer()


def normalize_text(text: str) -> str:
    if not text:
        return ""

    text = unicodedata.normalize('NFD', text.lower())
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = unicodedata.normalize('NFC', text)

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words]

    return ' '.join(words)


def phrase_match_score(query, candidate):
    q = normalize_text(query)
    c = normalize_text(candidate)

    return fuzz.token_sort_ratio(q, c)


def get_context_prompt(user_input, domain=None):
    """
    Truy xuất ngữ cảnh và thuật ngữ từ cơ sở tri thức (RAG).
    """

    user_input_norm = normalize_text(user_input)

    # ----------------------------
    # Dynamic retrieval
    # ----------------------------

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

    # ----------------------------
    # Phrase-aware retrieval
    # ----------------------------

    tokens = user_input.split()

    bigrams = [
        f"{tokens[i]} {tokens[i+1]}"
        for i in range(len(tokens)-1)
    ]

    queries = list(set([
        user_input,
        user_input_norm,
        *bigrams
    ]))

    # ----------------------------
    # Domain routing
    # ----------------------------

    target_collections = ["general_kb"]

    if domain:

        if "medical" in domain.lower() or "y tế" in domain.lower():
            target_collections.insert(0, "medical_kb")

        elif "finance" in domain.lower() or "kinh tế" in domain.lower():
            target_collections.insert(0, "economic_kb")

        elif "it" in domain.lower() or "công nghệ" in domain.lower():
            target_collections.insert(0, "technical_kb")

        else:
            target_collections = [
                "medical_kb",
                "economic_kb",
                "technical_kb",
                "general_kb"
            ]

    # ----------------------------
    # Query ChromaDB
    # ----------------------------

    all_docs = []
    all_metas = []
    all_distances = []

    seen_ids = set()

    for col_name in target_collections:

        try:
            col = client.get_collection(
                name=col_name,
                embedding_function=local_ef
            )

        except Exception:
            continue

        results = col.query(
            query_texts=queries,
            n_results=query_n_results
        )

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

    # ----------------------------
    # Candidate processing
    # ----------------------------

    processed_candidates = []

    for doc, meta, dist in zip(all_docs, all_metas, all_distances):

        text_from_db = doc

        current_score = 1.0 - (dist / 2.0)

        # Phrase boost
        word_list = text_from_db.split()

        if 2 <= len(word_list) <= 4:
            current_score += 0.25

        # Fuzzy boost
        similarity = phrase_match_score(
            user_input,
            text_from_db
        )

        if similarity > 90:
            current_score += 0.5

        elif similarity > 80:
            current_score += 0.3

        processed_candidates.append({
            "text": text_from_db,
            "metadata": meta,
            "dist": dist,
            "score": current_score
        })

    # ----------------------------
    # Pre-filter
    # ----------------------------

    processed_candidates.sort(
        key=lambda x: x["dist"]
    )

    top_candidates = processed_candidates[:25]

    # ----------------------------
    # Reranker bypass
    # ----------------------------

    reranked = []

    BYPASS_DISTANCE_THRESHOLD = 0.4

    is_bypass = False

    if len(top_candidates) > 0:

        top_5_distances = [
            item["dist"]
            for item in top_candidates[:5]
        ]

        avg_dist = sum(top_5_distances) / len(top_5_distances)

        if avg_dist <= BYPASS_DISTANCE_THRESHOLD:
            is_bypass = True

    # ----------------------------
    # Bypass reranker
    # ----------------------------

    if is_bypass:

        print("⚡ Bypassing Reranker")

        for item in top_candidates:

            reranked.append({
                "text": item["text"],
                "metadata": item["metadata"],
                "score": item["score"],
                "is_bypass": True
            })

    else:

        hits = [
            [user_input, item["text"]]
            for item in top_candidates
        ]

        scores = reranker.predict(hits)

        for i in range(len(top_candidates)):

            item = top_candidates[i]

            reranked.append({
                "text": item["text"],
                "metadata": item["metadata"],
                "score": float(scores[i]),
                "is_bypass": False
            })

        reranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

    # ----------------------------
    # Build prompt
    # ----------------------------

    tm_context = "[NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]\n"

    glossary_context = "[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]\n"

    found_tm = False
    found_glos = False

    seen_texts = set()

    # ----------------------------
    # Glossary extraction
    # ----------------------------

    for item in reranked:

        text = item["text"]

        meta = item["metadata"]

        score = item["score"]

        is_bypass = item["is_bypass"]

        item_domain = str(meta.get("domain", "general"))

        vi = meta.get("vietnamese", "N/A")

        is_glossary = (
            meta.get("type") == "term"
            or "glossary" in item_domain.lower()
        )

        threshold_met = (
            (is_bypass and score >= 0.7)
            or
            (not is_bypass and score >= 0.5)
        )

        if is_glossary and threshold_met:

            text_norm = normalize_text(text)

            pattern = (
                r'\b'
                + re.escape(text_norm).replace(r'\ ', r'\s+')
                + r'\b'
            )

            if re.search(pattern, user_input_norm):

                term_entry = f"- {text} => {vi}\n"

                if term_entry not in glossary_context:

                    glossary_context += term_entry

                    found_glos = True

                    seen_texts.add(text_norm)

    # ----------------------------
    # Context extraction
    # ----------------------------

    context_count = 0

    for item in reranked:

        if context_count >= max_context:
            break

        text = item["text"]

        text_key = normalize_text(text)

        if text_key in seen_texts:
            continue

        meta = item["metadata"]

        item_domain = str(meta.get("domain", "general"))

        vi = meta.get("vietnamese", "N/A")

        is_glossary = (
            meta.get("type") == "term"
            or "glossary" in item_domain.lower()
        )

        if not is_glossary:

            tm_context += (
                f"- Tiếng Anh: {text}\n"
                f"  Nghĩa: {vi}\n"
            )

            found_tm = True

            context_count += 1

            seen_texts.add(text_key)

    # ----------------------------
    # Final prompt
    # ----------------------------

    final_prompt = ""

    if found_tm:
        final_prompt += tm_context + "\n"

    if found_glos:
        final_prompt += glossary_context

    return (
        final_prompt
        if final_prompt
        else "Không tìm thấy thuật ngữ hay ngữ cảnh cụ thể."
    )


def format_qwen_prompt(
    user_input,
    context,
    domain="Đa lĩnh vực",
    terminology="Xem danh sách bên dưới",
    source_lang="English",
    target_lang="Vietnamese"
):
    """
    Định dạng prompt ChatML cho Qwen
    """

    system_content = system_prompt.format(
        domain=domain,
        terminology=terminology,
        context=context,
        source_lang=source_lang,
        target_lang=target_lang
    )

    return (
        f"<|im_start|>system\n"
        f"{system_content}"
        f"<|im_end|>\n"
        f"<|im_start|>user\n"
        f"Dịch đoạn văn này: {user_input}"
        f"<|im_end|>\n"
        f"<|im_start|>assistant\n"
    )


def check_semantic_cache(user_input, threshold=0.85):
    """
    Kiểm tra semantic cache
    """

    try:

        col = client.get_collection(
            name="translation_cache",
            embedding_function=local_ef
        )

        results = col.query(
            query_texts=[user_input],
            n_results=1
        )

        if (
            results["distances"]
            and results["distances"][0]
            and results["distances"][0][0] < (1 - threshold)
        ):

            return results["metadatas"][0][0]["translation"]

    except Exception:
        pass

    return None


def add_to_cache(user_input, translation):
    """
    Lưu cache
    """

    try:

        col = client.get_or_create_collection(
            name="translation_cache",
            embedding_function=local_ef
        )

        import uuid

        col.add(
            ids=[str(uuid.uuid4())],
            documents=[user_input],
            metadatas=[{
                "translation": translation
            }]
        )

    except Exception as e:

        print(f"⚠️ Không thể lưu cache: {e}")