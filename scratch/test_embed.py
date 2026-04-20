import chromadb
from chromadb.utils import embedding_functions

def test_embedding():
    print("Initializing embedding function...")
    local_ef = embedding_functions.DefaultEmbeddingFunction()
    print("Embedding a test string...")
    res = local_ef(["hello world"])
    print(f"Success! Result length: {len(res[0])}")

if __name__ == "__main__":
    test_embedding()
