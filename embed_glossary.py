import json
import chromadb
from chromadb.utils import embedding_functions

# 1. Khai báo hàm Embedding Local (MiniLM) của ChromaDB chạy offline trên máy cấu hình yếu
local_ef = embedding_functions.DefaultEmbeddingFunction()

# 2. Đọc file JSON Glossary hiện tại
with open("glossary.json", "r", encoding="utf-8") as f:
    glossary = json.load(f)

documents = []
metadatas = []
ids = []

for idx, (term, data) in enumerate(glossary.items()):
    documents.append(term)
    metadatas.append({
        "translation": str(data["translation"]),
        "rule": str(data["rule"])
    })
    ids.append(f"glossary_{idx}")

# 3. Khởi tạo Client và Collection mới cho Knowledge Base
client = chromadb.PersistentClient(path="./VectorDB_Gemini")

collection = client.get_or_create_collection(
    name="translator_glossary_kb_local",
    embedding_function=local_ef
)

# 4. Nạp dữ liệu Glossary vào DB theo Batch (Không còn lo Rate Limit)
batch_size = 1000 # Có thể nạp 1000 từ một lúc
print(f"Bắt đầu nhúng {len(documents)} thuật ngữ bằng Local Model vào VectorDB...")
i = 0
while i < len(documents):
    end = min(i + batch_size, len(documents))
    collection.upsert(
        documents=documents[i:end],
        metadatas=metadatas[i:end],
        ids=ids[i:end]
    )
    print(f">>> Đã xong thuật ngữ: {end}/{len(documents)}")
    i += batch_size

print("✅ Đã lưu toàn bộ Knowledge Base bằng mô hình MiniLM rêng biệt! (Collection: translator_glossary_kb_local)")
