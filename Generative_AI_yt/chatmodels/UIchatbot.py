import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

Prompt = """
You are Dr. Harshit.

Rules:
- Answer only medical questions.
- Keep responses under 120 words.
- Use bullet points only when necessary.
- Do not explain unnecessary details.
- If the user asks a non-medical question, reply:
'I only answer medical questions.'
"""

st.set_page_config(
    page_title="Harshit Chat Application",
    page_icon="💬",
    layout="wide",
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top left, #1b1f2b 0%, #0e1016 60%);
    }

    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #34d399, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        letter-spacing: -0.5px;
    }

    .sub-title {
        text-align: center;
        color: #8b93a7;
        font-size: 0.95rem;
        margin-bottom: 30px;
    }

    /* chat bubbles */
    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 12px 16px;
        margin-bottom: 10px;
        border: 1px solid rgba(255,255,255,0.06);
        box-shadow: 0 2px 10px rgba(0,0,0,0.25);
    }

    /* user bubble */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: linear-gradient(135deg, #1e293b, #1b2436);
        border: 1px solid rgba(56,189,248,0.25);
    }

    /* assistant bubble */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: linear-gradient(135deg, #14241d, #142226);
        border: 1px solid rgba(52,211,153,0.25);
    }

    /* avatar circles */
    [data-testid="chatAvatarIcon-user"] {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9) !important;
    }
    [data-testid="chatAvatarIcon-assistant"] {
        background: linear-gradient(135deg, #34d399, #059669) !important;
    }

    section[data-testid="stSidebar"] {
        background: #11131c;
        border-right: 1px solid rgba(255,255,255,0.06);
    }

    .history-item {
        background: rgba(255,255,255,0.04);
        border-radius: 10px;
        padding: 9px 12px;
        margin-bottom: 7px;
        font-size: 0.84rem;
        color: #cbd5e1;
        line-height: 1.4;
    }
    .history-user { border-left: 3px solid #38bdf8; }
    .history-bot { border-left: 3px solid #34d399; }

    [data-testid="stChatInput"] {
        border-radius: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💬 Harshit Chat Application</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ask me your medical questions, powered by Gemini ✨</div>', unsafe_allow_html=True)

# ---------- Model ----------
if "model" not in st.session_state:
    st.session_state.model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        max_output_tokens=150,
        
    )

model = st.session_state.model

# ---------- Session State (message history) ----------
if "message" not in st.session_state:
    st.session_state.message = [
        SystemMessage(content=Prompt)
    ]

USER_AVATAR = "🙋"
BOT_AVATAR = "🤖"

# ---------- Sidebar ----------
with st.sidebar:
    st.header("⚙️ Options")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.message = [
            SystemMessage(content=PERSONA)
        ]
        st.rerun()
    st.caption("Type `exit`, `quit`, or `byt` to end the chat.")

    st.markdown("---")
    st.subheader("🕓 Conversation History")

    history_msgs = [m for m in st.session_state.message if not isinstance(m, SystemMessage)]

    if not history_msgs:
        st.caption("No messages yet.")
    else:
        for msg in history_msgs:
            if isinstance(msg, HumanMessage):
                st.markdown(
                    f'<div class="history-item history-user">{USER_AVATAR} {msg.content}</div>',
                    unsafe_allow_html=True,
                )
            elif isinstance(msg, AIMessage):
                preview = msg.content if len(msg.content) <= 120 else msg.content[:120] + "..."
                st.markdown(
                    f'<div class="history-item history-bot">{BOT_AVATAR} {preview}</div>',
                    unsafe_allow_html=True,
                )

# ---------- Render chat history (main area) ----------
for msg in st.session_state.message:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown(msg.content)
    # SystemMessage is intentionally not displayed

# ---------- Chat input ----------
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.message.append(HumanMessage(content=prompt))
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    if prompt.lower() in ['exit', 'quit', 'byt']:
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown("👋 Goodbye!")
        st.stop()
    else:
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            with st.spinner("Thinking..."):
                try:
                    response = model.invoke(st.session_state.message)
                    st.markdown(response.content)
                except Exception as e:
                    if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                        st.error("⚠️ Daily free quota khatam ho gaya hai. Thodi der baad try karo ya billing enable karo.")
                    else:
                        st.error(f"Kuch error aaya: {e}")
                    st.stop()
        st.session_state.message.append(AIMessage(content=response.content))
        st.rerun()