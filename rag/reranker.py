from sentence_transformers import CrossEncoder

class CrossEncoderReranker:
    """Reranks ANN retrieved chunks using a Cross-Encoder for maximum RAG precision"""
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, retrieved_docs: list, top_n: int = 2) -> list:
        if not retrieved_docs:
            return []
        
        pairs = [[query, doc["clause_text"]] for doc in retrieved_docs]
        scores = self.model.predict(pairs)
        
        for i, doc in enumerate(retrieved_docs):
            doc["rerank_score"] = float(scores[i])
            
        # Sort descending by cross-encoder score
        reranked = sorted(retrieved_docs, key=lambda x: x["rerank_score"], reverse=True)
        return reranked[:top_n]