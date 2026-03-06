from langchain.agents import create_agent
from langchain_groq import ChatGroq

from agents.tools import search_internal_docs, web_search
from config import GROQ_API_KEY


def build_agent():

    # Groq LLM
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="openai/gpt-oss-120b",
        temperature=0.2
    )

    # Tools
    tools = [
        search_internal_docs,
        web_search
    ]

    # Create LangChain agent
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are an AI mentor helping new engineers understand software systems."
    )

    return agent