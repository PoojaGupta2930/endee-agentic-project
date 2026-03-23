from embeddings import get_embedding
from endee_client import search_vector
import requests


def ask_llm(prompt):

    url = "http://ollama:11434/api/generate"

    data = {
        "model": "orca-mini",
        "prompt": prompt,
        "stream": False,
    }

    r = requests.post(url, json=data)

    return r.json()["response"]


def rag(question):

    vec = get_embedding(question)

    results = search_vector(vec)

    if isinstance(results, dict) and "error" in results:
        return results["error"]

    context = ""

    for r in results["results"]:
        context += r["metadata"]["text"] + "\n"

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    return ask_llm(prompt)