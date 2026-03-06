import streamlit as st
from agents.agent import build_agent

st.set_page_config(
    page_title="AI Mentor",
    page_icon="🤖",
    layout="wide"
)

agent = build_agent()

# ---------------- CSS UI ----------------

st.markdown("""
<style>

.stApp {
background: linear-gradient(-45deg,#020617,#0f172a,#020617,#1e293b);
background-size: 400% 400%;
animation: gradientMove 12s ease infinite;
color:white;
}

@keyframes gradientMove {
0% {background-position:0% 50%;}
50% {background-position:100% 50%;}
100% {background-position:0% 50%;}
}

.title {
font-size:48px;
font-weight:700;
background: linear-gradient(90deg,#6366f1,#22c55e,#38bdf8);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
text-align:center;
}

.glass {
background: rgba(255,255,255,0.05);
backdrop-filter: blur(16px);
border-radius:16px;
padding:20px;
border:1px solid rgba(255,255,255,0.08);
}

.card {
background: linear-gradient(135deg,#6366f1,#8b5cf6);
padding:20px;
border-radius:14px;
text-align:center;
font-weight:600;
transition:0.3s;
cursor:pointer;
}

.card:hover{
transform: translateY(-6px) scale(1.03);
box-shadow:0 15px 40px rgba(0,0,0,0.4);
}

.status-dot{
width:10px;
height:10px;
background:#22c55e;
border-radius:50%;
display:inline-block;
animation:pulse 1.5s infinite;
margin-right:6px;
}

@keyframes pulse{
0%{box-shadow:0 0 0 0 rgba(34,197,94,0.7);}
70%{box-shadow:0 0 0 10px rgba(34,197,94,0);}
100%{box-shadow:0 0 0 0 rgba(34,197,94,0);}
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🤖 AI Mentor")

    st.markdown("---")

    st.markdown("### ⚙️ System")

    st.markdown("⚡ **Model:** Groq")
    st.markdown("🦜 **Framework:** LangChain")
    st.markdown("📚 **Knowledge:** RAG")
    st.markdown("🔎 **Search:** Tavily")

    st.markdown("---")

    st.markdown(
        '<span class="status-dot"></span>System Online',
        unsafe_allow_html=True
    )

# ---------------- HEADER ----------------

st.markdown('<div class="title">AI Mentor for Engineers</div>', unsafe_allow_html=True)

st.markdown(
"""
<div class="glass">
Ask questions about <b>software engineering, architecture, infrastructure, and development tools.</b>
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- FEATURE CARDS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">⚡ Groq Inference</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">🧠 AI Knowledge Engine</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">🔎 Web + Docs Intelligence</div>', unsafe_allow_html=True)

st.divider()

# ---------------- CHAT MEMORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- CHAT INPUT ----------------

prompt = st.chat_input("Ask an engineering question...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = agent.invoke({
                "messages":[{"role":"user","content":prompt}]
            })

        answer = response["messages"][-1].content

        st.markdown(answer)

    st.session_state.messages.append({
        "role":"assistant",
        "content":answer
    })