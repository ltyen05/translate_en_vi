import chromadb
from chromadb.utils import embedding_functions
import re
from sentence_transformers import CrossEncoder

#1.
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

# Sử dụng mô hình Embedding mặc định (Local MiniLM - đồng bộ với master_indexer.py)
local_ef = embedding_functions.DefaultEmbeddingFunction()

client = chromadb.PersistentClient(path="./VectorDB_Gemini")

# Kết nối tới Collection chính được tạo bởi master_indexer.py
collection = client.get_or_create_collection(
    name="multi_domain_rag_kb",
    embedding_function=local_ef
)

# KHỞI TẠO RERANKER (Multi-stage Retrieval)
print("Loading Reranker model (cross-encoder/ms-marco-MiniLM-L-6-v2)...")
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def get_context_prompt(user_input, domain=None):
    # Prepare metadata filter if domain is provided
    where_filter = {"domain": domain} if domain else None

    # --- STAGE 1: RETRIEVAL (Vector Search) ---
    # Lấy 50 ứng viên tiềm năng nhất (Recall cao)
    retrieval_results = collection.query(
        query_texts=[user_input],
        n_results=50,
        where=where_filter
    )

    if not retrieval_results.get("documents") or not retrieval_results["documents"][0]:
        return "Không có ngữ cảnh bổ trợ đặc biệt nào được tìm thấy."

    candidates = retrieval_results["documents"][0]
    metadatas = retrieval_results["metadatas"][0]

    # --- STAGE 2: RERANKING (Cross-Encoding) ---
    # Chuẩn bị cặp (Query, Document) để chấm điểm
    hits = []
    for i in range(len(candidates)):
        hits.append([user_input, candidates[i]])
    
    # Tính toán relevance scores
    scores = reranker.predict(hits)
    
    # Kết hợp Score với dữ liệu và sắp xếp lại
    reranked_results = []
    for i in range(len(candidates)):
        reranked_results.append({
            "text": candidates[i],
            "metadata": metadatas[i],
            "score": scores[i]
        })
    
    # Sắp xếp giảm dần theo điểm số
    reranked_results = sorted(reranked_results, key=lambda x: x["score"], reverse=True)
    
    # Chỉ lấy Top 10 kết quả tốt nhất sau khi Rerank
    top_results = reranked_results[:10]

    # --- PHẦN TRÌNH BÀY PROMPT ---
    tm_context = "[NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]\n"
    glossary_context = "[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]\n"
    
    user_input_lower = user_input.lower()

    for item in top_results:
        text = item["text"]
        meta = item["metadata"]
        vi_meaning = meta.get("vi", "N/A")
        item_domain = meta.get("domain", "General")

        # Phân loại hiển thị dựa trên độ dài (Glossary vs Context)
        if len(text.split()) <= 4:
            # Kiểm tra chính xác từ đó có trong câu không (Regex)
            pattern = r'\b' + re.escape(text.lower()) + r'\b'
            if re.search(pattern, user_input_lower):
                glossary_context += f"- '{text}': {vi_meaning} (Lĩnh vực: {item_domain})\n"
        else:
            tm_context += f"- Tiếng Anh: {text}\n  Nghĩa: {vi_meaning}\n"

    return f"{tm_context}\n{glossary_context}"

def format_qwen_prompt(user_input, context, domain="Đa lĩnh vực", terminology="Xem danh sách bên dưới", source_lang="English", target_lang="Vietnamese"):
    """
    Định dạng prompt theo chuẩn ChatML (Qwen) để mô hình nhận diện tốt nhất ngữ cảnh.
    """
    system_content = system_prompt.format(
        domain=domain,
        terminology=terminology,
        context=context,
        source_text=user_input,
        source_lang=source_lang,
        target_lang=target_lang
    )
    
    # Qwen format (ChatML)
    full_prompt = f"<|im_start|>system\n{system_content}<|im_end|>\n"
    full_prompt += f"<|im_start|>user\nDịch câu này: {user_input}<|im_end|>\n"
    full_prompt += "<|im_start|>assistant\n"
    
    return full_prompt