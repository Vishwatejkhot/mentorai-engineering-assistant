import os 
from dotenv import load_dotenv 

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY or not TAVILY_API_KEY:
    raise ValueError("Please set GROQ_API_KEY and TAVILY_API_KEY in your .env file")