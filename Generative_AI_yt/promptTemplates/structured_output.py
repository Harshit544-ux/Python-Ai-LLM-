from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import Optional, List

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_tokens=1000
)

# Define the expected output structure using Pydantic
class Movie(BaseModel):
    title: str
    release_year: Optional[str] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[str] = None
    summary: str

# Create a parser to convert LLM output into a Movie object
parser = PydanticOutputParser(pydantic_object=Movie)

# Create a prompt template with system and user messages
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract structured information from the user's movie-related query.

{format_instructions}
"""
        ),
        ("human", "{movie_query}")
    ]
)

# Take movie description as input from the user
movie_query = input("Enter your paragraph: ")

# Format the prompt by injecting the user input and parser instructions
final_prompt = prompt_template.invoke(
    {
        "movie_query": movie_query,
        "format_instructions": parser.get_format_instructions()
    }
)

# Send the prompt to the Gemini model
response = model.invoke(final_prompt)

# Parse the model response into a validated Pydantic object
movie = parser.parse(response.content)

# Display the extracted movie information in JSON format
print("\n🎬 Movie Information\n")
print(movie.model_dump_json(indent=4))