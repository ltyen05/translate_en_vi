import pandas as pd
import chromadb
from chromadb.utils import embedding_functions # Cần import thêm cái này

# 1. Khai báo hàm Embedding của Gemini
# Thạch nhớ thay API Key thật của bạn vào nhé
gemini_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key="AIzaSyDyNfgA0Iz3J41wSQuNI-M3Z4J50HglruY",
    model_name="models/gemini-embedding-001"
)

# 2. Đọc dữ liệu
df = pd.read_csv("clean_dataset.csv").dropna(subset=['en', 'vi']).head(5000)

documents = df['en'].tolist()
metadatas = [{"vi": str(row['vi'])} for _, row in df.iterrows()]
ids = [f"id_{i}" for i in range(len(df))]

# 3. Khởi tạo Client và Collection với Gemini EF
client = chromadb.PersistentClient(path="./VectorDB_Gemini")

# QUAN TRỌNG: Phải truyền embedding_function vào đây
collection = client.get_or_create_collection(
    name="translator_gemini_context",
    embedding_function=gemini_ef
)

# 4. Nạp dữ liệu theo Batch
batch_size = 50 # Dùng Gemini API thì nên để batch nhỏ hơn để tránh lỗi quá tải (Rate Limit)
for i in range(0, len(documents), batch_size):
    end = min(i + batch_size, len(documents))
    collection.add(
        documents=documents[i:end],
        metadatas=metadatas[i:end],
        ids=ids[i:end]
    )
    print(f">>> Đã xong: {end}/{len(documents)}")

print("✅ Đã nâng cấp lên Gemini Embedding thành công!")