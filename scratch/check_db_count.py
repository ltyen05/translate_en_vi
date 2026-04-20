import chromadb
from chromadb.utils import embedding_functions

DB_PATH = "./VectorDB_Gemini"
COLLECTION_NAME = "multi_domain_rag_kb"

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_collection(name=COLLECTION_NAME)
print(f"Total documents in collection: {collection.count()}")
