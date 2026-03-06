# 🧠 Mentorai-engineering-assistant

MentorAI is an AI-powered engineering mentor designed to help developers
understand software engineering concepts, system architecture, and
development practices.\
It uses Retrieval-Augmented Generation (RAG) and agent-based reasoning
to answer questions using both internal documentation and external
knowledge.

------------------------------------------------------------------------
## 🌐 Live Demo

🚀 Try the deployed application here:

👉 https://mentorai-engineering-assistant.streamlit.app
------------------------------------------------------------------------

## 🚀 Features

-   🤖 AI mentor for software engineers
-   📚 Retrieval-Augmented Generation (RAG)
-   🧠 Agent-based reasoning using LangChain
-   🔎 Web search integration using Tavily
-   ⚡ Fast LLM inference powered by Groq
-   💬 Interactive chat interface built with Streamlit
-   📄 Supports structured responses (tables, lists, code blocks)

------------------------------------------------------------------------

## 🏗️ Architecture

User Question\
↓\
Streamlit UI\
↓\
LangChain Agent\
↓\
Tool Selection

• RAG Retriever (Vector Database)\
• Tavily Web Search

↓\
Groq LLM\
↓\
Final Response

------------------------------------------------------------------------

## 🧰 Tech Stack

  Technology       Purpose
  ---------------- -----------------------
  Streamlit        Frontend UI
  LangChain        Agent orchestration
  Groq             Fast LLM inference
  FAISS / Chroma   Vector database
  Tavily           Web search API
  Python           Core backend language

------------------------------------------------------------------------

## 📂 Project Structure

mentorai-engineering-assistant/

├── agents/\
│ ├── agent.py\
│ └── tools.py

├── rag/\
│ ├── rag_chain.py\
│ └── vector_store.py

├── data/\
│ ├── onboarding_guide.txt\
│ ├── system_architecture.txt\
│ ├── microservices.txt\
│ ├── api_design.txt\
│ ├── docker_basics.txt\
│ ├── kubernetes_basics.txt\
│ ├── git_workflow.txt\
│ ├── coding_standards.txt\
│ ├── database_design.txt\
│ └── security_practices.txt

├── prompts/\
│ └── mentor_prompt.txt

├── config.py\
├── app.py\
├── requirements.txt\
├── .env.example\
└── README.md

------------------------------------------------------------------------

## 📚 Knowledge Base

MentorAI uses internal engineering documentation covering:

-   Engineer onboarding process
-   System architecture fundamentals
-   Microservices architecture
-   API design best practices
-   Docker containerization
-   Kubernetes orchestration
-   Git workflows
-   Coding standards
-   Database design principles
-   Security best practices

These documents are embedded into a vector database and retrieved during
question answering.

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone the repository

git clone
https://github.com/yourusername/mentorai-engineering-assistant.git\
cd mentorai-engineering-assistant

### 2. Create a virtual environment

python -m venv .venv

Activate:

Windows: .venv`\Scripts`{=tex}`\activate  `{=tex}

Mac/Linux: source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure API keys

Create a `.env` file:

GROQ_API_KEY=your_groq_api_key\
TAVILY_API_KEY=your_tavily_api_key

### 5. Run the application

streamlit run app.py

------------------------------------------------------------------------

## 💡 Example Questions

-   Explain system architecture in simple terms
-   What is microservices architecture?
-   How does Docker work?
-   What is CI/CD?
-   Explain event-driven architecture
-   What security practices should engineers follow?

------------------------------------------------------------------------

## 📜 License

This project is licensed under the MIT License.

------------------------------------------------------------------------

## ⭐ If you found this project useful

Consider giving the repository a star ⭐ on GitHub!
