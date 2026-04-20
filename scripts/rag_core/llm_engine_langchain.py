import os
from typing import Any, List, Optional, Mapping
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
import requests

# --- 1. Modular Translation LLM (Dùng chung cho cả Local File và API) ---
class ModularTranslationLLM(LLM):
    mode: str = "api"  # "api" hoặc "local"
    endpoint: str = "" # URL cho API hoặc Path cho Local file
    api_key: Optional[str] = None
    
    # Placeholder cho local model
    _local_engine: Any = None 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.mode == "local":
            self._init_local_model()

    def _init_local_model(self):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch
        print(f"LangChain: Đang nạp mô hình cục bộ từ {self.endpoint}...")
        try:
            # Logic nạp file trọng số đơn giản
            self._local_engine = {
                "tokenizer": AutoTokenizer.from_pretrained(self.endpoint, trust_remote_code=True),
                "model": AutoModelForCausalLM.from_pretrained(
                    self.endpoint, 
                    torch_dtype=torch.float16 if torch.backends.mps.is_available() else torch.float32,
                    device_map="auto",
                    trust_remote_code=True
                )
            }
            print("✅ Nạp mô hình cục bộ thành công.")
        except Exception as e:
            print(f"❌ Không thể nạp mô hình: {e}")

    @property
    def _llm_type(self) -> str:
        return "modular_translation_llm"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        # --- CHẾ ĐỘ KẾT NỐI API ---
        if self.mode == "api":
            headers = {"Content-Type": "application/json"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            
            payload = {"prompt": prompt, "max_tokens": 512}
            try:
                response = requests.post(self.endpoint, json=payload, headers=headers)
                result = response.json()
                return result.get("translation") or result.get("response") or str(result)
            except Exception as e:
                return f"[LỖI API] {e}"

        # --- CHẾ ĐỘ NẠP FILE TRỌNG SỐ ---
        elif self.mode == "local":
            if not self._local_engine:
                return "[LỖI] Chưa nạp được mô hình cục bộ."
            
            tokenizer = self._local_engine["tokenizer"]
            model = self._local_engine["model"]
            
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            outputs = model.generate(**inputs, max_new_tokens=512)
            return tokenizer.decode(outputs[0], skip_special_tokens=True)

        return "[LỖI] Chế độ hoạt động không hợp lệ."

# --- 2. Hỗ trợ RAG Retriever (Giữ nguyên logic LangChain mạnh mẽ) ---
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

def get_langchain_retriever(db_path="./VectorDB_Gemini", collection_name="multi_domain_rag_kb"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=db_path, collection_name=collection_name, embedding_function=embeddings)
    
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": 50})
    
    # Reranker vẫn rất quan trọng để đảm bảo độ chính xác
    model = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")
    compressor = CrossEncoderReranker(model=model, top_n=10)
    
    return ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base_retriever)
