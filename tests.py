import unittest
import os
import pandas as pd
from ann.embedder import TextEmbedder
from ann.hnsw_index import HNSWVectorIndex
from rag.retriever import ANNRetriever
from rag.reranker import CrossEncoderReranker

class TestVendorCompliancePipeline(unittest.TestCase):
    
    def test_embedder_dimensions(self):
        embedder = TextEmbedder()
        embeddings = embedder.encode_texts(["Payment terms net 30 days."])
        self.assertEqual(embeddings.shape[1], 384)

    def test_hnsw_and_retrieval(self):
        embedder = TextEmbedder()
        docs = [
            {"vendor_name": "TestCorp A", "clause_text": "Payment terms shall be net 30 days."},
            {"vendor_name": "TestCorp B", "clause_text": "Unlimited liability on vendor side."}
        ]
        embeddings = embedder.encode_texts([d["clause_text"] for d in docs])
        
        hnsw = HNSWVectorIndex(dimension=384, M=16)
        hnsw.build_index(embeddings, docs)
        
        retriever = ANNRetriever(embedder, hnsw)
        results = retriever.retrieve("payment", top_k=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["vendor_name"], "TestCorp A")

    def test_cross_encoder_reranker(self):
        reranker = CrossEncoderReranker()
        query = "Payment terms must not exceed net 30 days."
        retrieved_docs = [
            {"vendor_name": "TestCorp A", "clause_text": "Payment terms shall be net 90 days."},
            {"vendor_name": "TestCorp B", "clause_text": "Payment terms shall be net 30 days."}
        ]
        reranked = reranker.rerank(query, retrieved_docs, top_n=1)
        self.assertEqual(len(reranked), 1)
        self.assertIn("rerank_score", reranked[0])
        print("All end-to-end component tests passed successfully!")

if __name__ == "__main__":
    unittest.main()