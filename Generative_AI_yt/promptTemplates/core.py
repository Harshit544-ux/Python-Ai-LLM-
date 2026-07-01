from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_tokens=1000
)

# Create Prompt Template
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
            "Extract the following information from the user's query:"
            "{movie_query}"
        )
    ]
)

# User Input
movie_query = input("Enter your paragraph : ")

final_prompt =prompt_template.invoke({"movie_query": movie_query})

# Generate Response
response = model.invoke(final_prompt)

# Print Response
print("\n🎬 Movie Information\n")
print(response.content)