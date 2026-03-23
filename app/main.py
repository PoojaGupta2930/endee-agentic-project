from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class VectorQuery(BaseModel):
    vector: list


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/search")
def search(data: VectorQuery):

    # correct format for rag.py
    return {
        "results": [
            {"metadata": {"text": "docker backend working"}},
            {"metadata": {"text": "search ok"}}
        ]
    }