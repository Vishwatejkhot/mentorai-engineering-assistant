from langchain_community.vectorstores.faiss import FAISS
from rag.embeddings import get_embeddings

def load_vectorstore():

    embeddings = get_embeddings()

    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db