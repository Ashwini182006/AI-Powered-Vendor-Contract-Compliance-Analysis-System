from sentence_transformers import SentenceTransformer
import numpy as np

class TextEmbedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dimension = 384

    def encode_texts(self, texts: list) -> np.ndarray:
        # Progress bar disabled for clean execution
        embeddings = self.model.encode(texts, show_progress_bar=False)
        return np.array(embeddings).astype("float32")