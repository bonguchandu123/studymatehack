# from sentence_transformers import SentenceTransformer
# import faiss
# import numpy as np

# class EmbeddingRetriever:
#     def __init__(self, model_name="all-MiniLM-L6-v2"):
#         # DO NOT manually call .to("cpu") or .to(device) — let SentenceTransformer handle it
#         self.model = SentenceTransformer(model_name, cache_folder="./hf-cache")

#         self.index = faiss.IndexFlatL2(384)
#         self.chunks = []

#     def index_chunks(self, chunks):
#         embeddings = self.model.encode(chunks)
#         self.index.add(np.array(embeddings).astype("float32"))
#         self.chunks = chunks

#     def get_top_k_chunks(self, query, k=3):
#         q_emb = self.model.encode([query])
#         D, I = self.index.search(np.array(q_emb).astype("float32"), k)
#         return [self.chunks[i] for i in I[0] if i < len(self.chunks)]



from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class EmbeddingRetriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(384)
        self.chunks = []

    def index_chunks(self, chunks):  
     if not chunks:  
        raise ValueError("No chunks provided for indexing.")  

     embeddings = self.model.encode(chunks, convert_to_numpy=True)  
     embeddings = np.array(embeddings).astype("float32")  

     if len(embeddings.shape) != 2:  
        raise ValueError(f"Expected 2D embeddings, got shape {embeddings.shape}")  

     self.index.add(embeddings)  
     self.chunks = chunks  

    def get_top_k_chunks(self, query, k=3):  
     if not self.chunks:  
        raise ValueError("No chunks indexed. Please run index_chunks first.")  

     q_emb = self.model.encode([query], convert_to_numpy=True)  
     q_emb = np.array(q_emb).astype("float32")  

     D, I = self.index.search(q_emb, k)  
     return [self.chunks[i] for i in I[0] if i < len(self.chunks)]

