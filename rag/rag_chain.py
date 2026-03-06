from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from rag.vector_store import load_vectorstore
from config import GROQ_API_KEY


def create_rag_chain():

    
    db = load_vectorstore()

    
    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10
        }
    )

    
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="openai/gpt-oss-120b",
        temperature=0.2,
        max_tokens=1024
    )

    # System prompt
    system_prompt = (
        "You are an AI mentor helping new engineers understand technical concepts. "
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Keep the answer clear and concise.\n\n"
        "Context:\n{context}"
    )

   
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}")
        ]
    )

    
    question_answer_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    
    rag_chain = create_retrieval_chain(
        retriever,
        question_answer_chain
    )

    return rag_chain