from functools import lru_cache

import numpy as np
from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


@lru_cache(maxsize=1)
def load_embedding_model():

    return SentenceTransformer(EMBEDDING_MODEL)


def semantic_similarity(
    text_a: str,
    text_b: str,
) -> float:

    if not text_a or not text_b:
        return 0.0

    model = load_embedding_model()

    embeddings = model.encode(
        [text_a, text_b],
        normalize_embeddings=True,
    )

    similarity = float(
        np.dot(
            embeddings[0],
            embeddings[1],
        )
    )

    similarity = max(0.0, min(1.0, similarity))

    return round(similarity * 100, 2)