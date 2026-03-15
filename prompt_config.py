import chromadb
from chromadb.utils import embedding_functions
import re

#1.
system_prompt = """
  Bạn là một Chuyên gia dịch Kỹ thuật cấp cao với 20 năm kinh nghiệm trong nghề. Chuyên môn của bạn là dịch tài liệu Công nghệ thông tin từ tiếng Anh sang tiếng Việt với độ chính xác tuyệt đối về thuật ngữ.
  Hệ thống đang sử dụng Hybrid RAG để truy xuất: Ngữ cảnh văn phong dịch từ Translation Memory và Quy tắc thuật ngữ từ Glossary.
  
  Bạn hãy tuân theo các quy tắc dịch thuật sau đây: 
  1. ƯU TIÊN THUẬT NGỮ: Tuân thủ tuyệt đối quy định trong [TỪ ĐIỂN THUẬT NGỮ (GLOSSARY)].
  2. VĂN PHONG DỊCH: Tham khảo cách hành văn trong [NGỮ CẢNH BẢN DỊCH VÍ DỤ (TRANSLATION MEMORY)] để dịch cho tự nhiên.
  3. ĐỊNH DẠNG: Giữ nguyên các đoạn mã (code snippets), tên hàm, biến, hoặc thẻ HTML/Markdown.
  4. PHONG CÁCH: Chuyên nghiệp, súc tích, phù hợp với kỹ sư phần mềm.
  
  Cấm: 
  1. Tuyệt đối không tự ý "sáng tạo" nghĩa mới cho các thuật ngữ đã được quy ước trong TỪ ĐIỂN THUẬT NGỮ.
  2. Bắt chước dập khuôn mà không suy nghĩ: Nếu bản dịch ví dụ có vẻ sai, hãy tự chọn cách dịch hay nhất.
  3. Không thêm các câu chào hỏi thừa thãi, chỉ xuất output là bản dịch.
"""

gemini_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key="AIzaSyDyNfgA0Iz3J41wSQuNI-M3Z4J50HglruY",
    model_name="models/gemini-embedding-001"
)

client = chromadb.PersistentClient(path="./VectorDB_Gemini")

# Khai báo thêm hàm Local Embedding
local_ef = embedding_functions.DefaultEmbeddingFunction()

# Collection 1: Dữ liệu mẫu (Translation Memory) - Vẫn giữ nguyên Gemini
collection = client.get_or_create_collection(
    name="translator_gemini_context",
    embedding_function=gemini_ef
)

# Collection 2: Bộ từ điển (Glossary Knowledge Base) - Đổi sang Local Model
glossary_collection = client.get_or_create_collection(
    name="translator_glossary_kb_local",
    embedding_function=local_ef
)

def get_context_prompt(user_input):
    # 1. Truy xuất Semantic VectorDB (Translation Memory) - Sử dụng try-except do Gemini API bị hết Limit
    context_prompt = None
    try:
        context_prompt = collection.query(
            query_texts=[user_input],
            n_results=1,
        )
    except Exception as e:
        print(f"[CẢNH BÁO] Không thể truy xuất Translation Memory do lỗi API Gemini: {str(e)[:100]}...")

    tm_context = "[NGỮ CẢNH BẢN DỊCH VÍ DỤ (TRANSLATION MEMORY)]\n"
    if context_prompt and context_prompt.get("documents") and context_prompt["documents"][0]:
        retrieved_en = context_prompt["documents"][0][0]
        retrieved_vi = context_prompt["metadatas"][0][0].get("vi", "")
        tm_context += f"English: {retrieved_en}\nVietnamese meaning: {retrieved_vi}\n"

    # 2. Truy xuất Keyword Glossary (Từ điển thuật ngữ) TỪ VECTOR DB
    glossary_context = "[TỪ ĐIỂN THUẬT NGỮ (GLOSSARY)]\n"
    user_input_lower = user_input.lower()
    found_terms = 0
    
    # Semantic Search: Lấy ngay top 30 thuật ngữ gần nghĩa nhất với câu của người dùng
    glossary_results = glossary_collection.query(
        query_texts=[user_input],
        n_results=30,
    )
    
    # Lọc lại chính xác (Regex matcher) với 30 kết quả trả về
    if glossary_results.get("documents") and glossary_results["documents"][0]:
        for i, term in enumerate(glossary_results["documents"][0]):
            meta = glossary_results["metadatas"][0][i]
            
            # Chỉ lấy nếu thuật ngữ đó CÓ THẬT SỰ xuất hiện trong câu (để tránh ảo giác RAG)
            pattern = r'\b' + re.escape(term.lower()) + r'\b'
            if re.search(pattern, user_input_lower):
                glossary_context += f"- '{term}': Dịch là '{meta['translation']}' -> Rule: {meta['rule']}\n"
                found_terms += 1
                
            # Giới hạn tối đa 15 thuật ngữ để tránh quá tải Prompt
            if found_terms >= 15:
                break
            
    if found_terms == 0:
         glossary_context += "- Không phát hiện thuật ngữ đặc biệt nào trong câu, hãy dịch tự do."

    # Kết hợp Hybrid Context
    retrieved_context = f"{tm_context}\n{glossary_context}"

    return retrieved_context