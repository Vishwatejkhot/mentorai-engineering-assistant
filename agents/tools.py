from langchain.tools import tool
from rag.rag_chain import create_rag_chain
from tavily import TavilyClient
from config import TAVILY_API_KEY

qa_chain = create_rag_chain()

@tool
def search_internal_docs(query: str):
    """Search internal engineering documentation"""
    return qa_chain.run(query)


@tool
def web_search(query: str):
    """Search the internet for engineering knowledge"""

    tavily = TavilyClient(api_key=TAVILY_API_KEY)

    result = tavily.search(query)

    return result