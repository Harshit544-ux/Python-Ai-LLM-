import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎥",
    layout="centered"
)

# ----------------------------
# Custom CSS (styling)
# ----------------------------
st.markdown(
    """
    <style>
    /* Overall background */
    .stApp {
        background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%);
    }

    /* Hide default streamlit chrome a bit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Header block */
    .hero {
        text-align: center;
        padding: 1.5rem 1rem 0.5rem 1rem;
    }
    .hero h1 {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff6b6b, #f7b733, #a56bff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero p {
        color: #b3b3c6;
        font-size: 1rem;
        margin-top: 0;
    }

    /* Text area */
    .stTextArea textarea {
        background-color: #1e1e30 !important;
        color: #f5f5f5 !important;
        border: 1px solid #3a3a55 !important;
        border-radius: 12px !important;
        font-size: 0.95rem !important;
    }
    .stTextArea textarea:focus {
        border: 1px solid #a56bff !important;
        box-shadow: 0 0 0 2px rgba(165, 107, 255, 0.25) !important;
    }

    .hint {
        color: #8a8aa3;
        font-size: 0.8rem;
        margin-top: -0.6rem;
        margin-bottom: 0.8rem;
    }

    /* Submit button */
    div.stFormSubmitButton button {
        background: linear-gradient(90deg, #ff6b6b, #a56bff);
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 1rem;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    div.stFormSubmitButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(165, 107, 255, 0.35);
        color: white;
    }

    /* Result card */
    .result-card {
        background-color: #1e1e30;
        border: 1px solid #3a3a55;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        margin-top: 1rem;
        color: #f5f5f5;
        line-height: 1.7;
    }
    .result-card h2 {
        margin-top: 0;
        font-size: 1.2rem;
        color: #f7b733;
    }

    .footer-caption {
        text-align: center;
        color: #6c6c85;
        font-size: 0.8rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

# ----------------------------
# Initialize Model
# ----------------------------
@st.cache_resource
def load_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        max_tokens=1000
    )

model = load_model()

# ----------------------------
# Prompt Template
# ----------------------------
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional Movie Information Extraction Assistant.

Your task is to extract structured information from the user's movie-related query.

Always return the information in the following format:

Movie Name:
Release Year:
Genre:
Director:
Main Cast:
Language:
Country:
Duration:
IMDb Rating:
Short Summary:

If any information is unavailable, return "Not Available".

Keep your response clear and well-formatted.
"""
        ),
        (
            "human",
            "Extract the following information from the user's query:\n{movie_query}"
        )
    ]
)

# ----------------------------
# Header
# ----------------------------
st.markdown(
    """
    <div class="hero">
        <h1>🎬 Movie Information Extractor</h1>
        <p>Enter a movie name, paragraph, or review — AI will pull out clean, structured details.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Input + Submit (wrapped in a form so Ctrl+Enter submits directly)
# ----------------------------
with st.form(key="movie_form", clear_on_submit=False):
    movie_query = st.text_area(
        "Movie Description",
        height=180,
        placeholder="Example:\nInterstellar is a 2014 science fiction film directed by Christopher Nolan starring Matthew McConaughey...",
        label_visibility="collapsed"
    )
    st.markdown('<p class="hint">💡 Tip: Press <b>Ctrl + Enter</b> inside the box to submit instantly.</p>', unsafe_allow_html=True)

    submitted = st.form_submit_button("🔍 Extract Information", use_container_width=True)

# ----------------------------
# Handle Submission
# ----------------------------
if submitted:
    if not movie_query.strip():
        st.warning("Please enter some movie information.")
        st.stop()

    with st.spinner("Extracting movie details..."):
        final_prompt = prompt_template.invoke({"movie_query": movie_query})
        response = model.invoke(final_prompt)

    st.success("Extraction Complete!")

    st.markdown(
        f"""
        <div class="result-card">
            <h2>📄 Extracted Information</h2>
            {response.content}
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Footer
# ----------------------------
st.markdown('<p class="footer-caption">Built with ❤️ using Streamlit + LangChain + Gemini</p>', unsafe_allow_html=True)