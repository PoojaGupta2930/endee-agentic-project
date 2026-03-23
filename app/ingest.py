from embeddings import get_embedding
from endee_client import add_vector
import uuid

texts = [

    "Artificial intelligence is simulation of human intelligence",

    "Machine learning is subset of AI",

    "Endee is vector database",

    "RAG means retrieval augmented generation",

    "Agentic AI can decide actions"
]

for t in texts:

    vec = get_embedding(t)

    add_vector(
        str(uuid.uuid4()),
        vec,
        t
    )

print("Inserted")