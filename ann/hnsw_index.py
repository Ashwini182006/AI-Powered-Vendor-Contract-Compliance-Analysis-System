import faiss
import numpy as np

class HNSWVectorIndex:
    """Uses FAISS HNSW (Hierarchical Navigable Small World) for ultra-fast graph-based ANN search"""
    def __init__(self, dimension: int = 384, M: int = 32):
        self.dimension = dimension
        self.index = faiss.IndexHNSWFlat(dimension, M)
        self.index.hnsw.efConstruction = 64
        self.index.hnsw.efSearch = 32
        self.metadata = []

    def build_index(self, embeddings: np.ndarray, docs: list):
        if len(embeddings) == 0:
            return
        self.index.add(embeddings)
        self.metadata.extend(docs)

    def search(self, query_vector: np.ndarray, top_k: int = 3) -> list:
        if self.index.ntotal == 0:
            return []
        distances, indices = self.index.search(query_vector, top_k)
        
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx != -1 and idx < len(self.metadata):
                res = self.metadata[idx].copy()
                res["ann_score"] = float(dist)
                results.append(res)
        return results