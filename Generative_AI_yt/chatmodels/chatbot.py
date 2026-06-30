import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load Environment Variables
load_dotenv()

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Mood based Ai chatbot",
    page_icon="🤖",
    layout="centered",
)

# -------------------- CUSTOM CSS --------------------

st.markdown(
    """
    <style>
        /* Hide default streamlit chrome */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        .main-title {
            text-align: center;
            font-size: 2.4rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }
        .sub-title {
            text-align: center;
            color: #888;
            margin-bottom: 1.8rem;
        }

        .mode-card {
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 14px;
            padding: 14px 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            background: rgba(255,255,255,0.03);
        }
        .mode-card:hover {
            transform: translateY(-3px);
            border-color: #ff4b4b;
        }
        .mode-emoji {
            font-size: 2rem;
        }

        .active-mode-banner {
            text-align: center;
            padding: 10px;
            border-radius: 10px;
            background: linear-gradient(90deg, rgba(255,75,75,0.15), rgba(255,75,75,0.05));
            border: 1px solid rgba(255,75,75,0.3);
            margin-bottom: 1rem;
            font-weight: 600;
        }

        div[data-testid="stChatMessage"] {
            border-radius: 14px;
            padding: 4px;
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- HEADER --------------------

st.markdown('<div class="main-title">🤖 Mood based AI chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Pick a personality and start chatting with Gemini</div>', unsafe_allow_html=True)

# -------------------- SESSION STATE --------------------

if "messages" not in st.session_state:
    st.session_state.messages = None

if "mode" not in st.session_state:
    st.session_state.mode = None

if "mode_label" not in st.session_state:
    st.session_state.mode_label = None

MODES = {
    "Angry": {
        "emoji": "😡",
        "prompt": "You are an angry AI agent. You respond aggressively and impatiently.",
    },
    "Funny": {
        "emoji": "😂",
        "prompt": "You are a very funny AI agent. You respond with jokes and funny replies.",
    },
    "Sad": {
        "emoji": "😢",
        "prompt": "You are a very sad AI agent. You respond sadly and heartbreakingly.",
    },
}

# -------------------- MODE SELECTION (only before chat starts) --------------------

if st.session_state.messages is None:
    st.write("")
    cols = st.columns(3)

    for col, (label, data) in zip(cols, MODES.items()):
        with col:
            st.markdown(
                f"""
                <div class="mode-card">
                    <div class="mode-emoji">{data['emoji']}</div>
                    <div>{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Choose {label}", key=f"btn_{label}", use_container_width=True):
                st.session_state.mode = data["prompt"]
                st.session_state.mode_label = f"{data['emoji']} {label}"
                st.session_state.messages = [SystemMessage(content=data["prompt"])]
                st.rerun()

# -------------------- CHAT SECTION --------------------

else:
    # Active mode banner + reset button
    top_left, top_right = st.columns([4, 1])
    with top_left:
        st.markdown(
            f'<div class="active-mode-banner">Active Mode: {st.session_state.mode_label}</div>',
            unsafe_allow_html=True,
        )
    with top_right:
        if st.button("🔄 New Chat", use_container_width=True):
            st.session_state.messages = None
            st.session_state.mode = None
            st.session_state.mode_label = None
            st.rerun()

    # Display Previous Chat
    for msg in st.session_state.messages[1:]:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user", avatar="🧑"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant", avatar=st.session_state.mode_label.split()[0]):
                st.write(msg.content)

    # User Input
    prompt = st.chat_input("Type your message...")

    if prompt:
        if prompt.lower() in ["exit", "quit", "bye"]:
            st.success("👋 Goodbye!")
            st.stop()

        # Store Human Message
        st.session_state.messages.append(HumanMessage(content=prompt))

        with st.chat_message("user", avatar="🧑"):
            st.write(prompt)

        # Gemini Response
        with st.chat_message("assistant", avatar=st.session_state.mode_label.split()[0]):
            with st.spinner("Thinking..."):
                response = model.invoke(st.session_state.messages)
            st.write(response.content)

        # Store AI Message
        st.session_state.messages.append(AIMessage(content=response.content))