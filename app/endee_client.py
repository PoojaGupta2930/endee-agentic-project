import requests

ENDEE = "http://api:8000"


def add_vector(id, vector, text):

    data = {
        "id": id,
        "vector": vector,
        "metadata": {"text": text}
    }

    requests.post(
        f"{ENDEE}/vectors",
        json=data
    )


def search_vector(vec):

    url = f"{ENDEE}/search"

    r = requests.post(
        url,
        json={"vector": vec}
    )

    print("STATUS:", r.status_code)
    print("TEXT:", r.text)

    try:
        return r.json()
    except Exception:
        return {"error": r.text}