from rag import rag


def agent(question):

    q = question.lower()

    # agent decision

    if "hello" in q:
        return "Hello I am Agentic AI"

    if "search" in q or "ai" in q or "what" in q:
        return rag(question)

    return rag(question)