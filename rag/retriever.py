class ANNRetriever:
    def __init__(self, embedder, hnsw_index):
        self.embedder = embedder
        self.hnsw_index = hnsw_index

    def retrieve(self, query: str, top_k: int = 3) -> list:
        query_vec = self.embedder.encode_texts([query])
        return self.hnsw_index.search(query_vec, top_k=top_k)