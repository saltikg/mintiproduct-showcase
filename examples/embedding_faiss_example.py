"""
Simple FAISS Vector Search Example (Safe Version)

This example demonstrates embedding text into vectors and performing
a similarity search using FAISS. This is a simplified and safe version
of the semantic search pipeline used in MintiProduct.

No production data, keys, or proprietary logic is included.
"""

import numpy as np
import faiss

# ----------------------------------------------------
# 1. Dummy Embedding Function (Safe)
# ----------------------------------------------------
def embed(text: str) -> np.ndarray:
    """
    Convert text into a simple numeric embedding.
    (Production uses real transformer embeddings.)
    """
    vec = np.zeros(64, dtype=np.float32)
    for idx, ch in enumerate(text[:64]):
        vec[idx] = ord(ch) % 50
    return vec


# ----------------------------------------------------
# 2. Build Index
# ----------------------------------------------------
texts = [
    "winter glow skincare routine",
    "how to stay motivated in November",
    "best holiday gift ideas",
    "cozy home decoration for winter",
]

embeddings = np.array([embed(t) for t in texts])

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


# ----------------------------------------------------
# 3. Query
# ----------------------------------------------------
query = "winter decoration ideas"
query_vec = embed(query).reshape(1, -1)

k = 2  # return top 2 results
distances, indices = index.search(query_vec, k)

print("Query:", query)
print("\nMost similar results:")

for rank, idx in enumerate(indices[0]):
    print(f"{rank+1}. {texts[idx]} (distance={distances[0][rank]:.2f})")
