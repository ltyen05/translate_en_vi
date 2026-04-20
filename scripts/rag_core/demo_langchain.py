import sys
import os
sys.path.append(os.getcwd())

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.run_models import RunnablePassthrough
from scripts.rag_core.llm_engine_langchain import ModularTranslationLLM, get_langchain_retriever
from prompt_config import format_qwen_prompt

def run_langchain_demo():
    print("=== DEMO DỊCH THUẬT: LANGCHAIN RAG PIPELINE (SIMPLIFIED) ===")
    
    # CHỌN MỘT TRONG HAI CHẾ ĐỘ:
    
    # Chế độ 1: Dùng API
    llm = ModularTranslationLLM(mode="api", endpoint="http://your-api-endpoint.com/translate")
    
    # Chế độ 2: Dùng file trọng số cục bộ
    # llm = ModularTranslationLLM(mode="local", endpoint="/Users/nguyenbaothach/Downloads/outputs/checkpoint-3000")

    retriever = get_langchain_retriever()
    
    # Sử dụng template từ prompt_config
    qwen_template = format_qwen_prompt("{source_text}", "{context}", 
                                     domain="{domain}", 
                                     terminology="{terminology}",
                                     source_lang="{source_lang}", 
                                     target_lang="{target_lang}")
    
    prompt = ChatPromptTemplate.from_template(qwen_template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": retriever | format_docs, 
            "source_text": RunnablePassthrough(),
            "domain": lambda x: "Medical",
            "terminology": lambda x: "Check glossary",
            "source_lang": lambda x: "English",
            "target_lang": lambda x: "Vietnamese"
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    test_query = "The patient is diagnosed with acute otitis media."
    print(f"\n[1] Câu tiếng Anh: {test_query}")
    print("\n[2] Thực thi LangChain Modular RAG...")
    
    try:
        # Lưu ý: Chế độ API sẽ lỗi nếu URL không tồn tại
        result = rag_chain.invoke(test_query)
        print(f"\n[3] KẾT QUẢ:\n{result}")
    except Exception as e:
        print(f"\n[!] Lưu ý: Demo lỗi vì chưa cấu hình API/Model thật: {e}")

if __name__ == "__main__":
    run_langchain_demo()
