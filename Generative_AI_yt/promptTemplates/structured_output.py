from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import Optional, List

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_tokens=1000
)

class Movie(BaseModel):
    title: str
    release_year: Optional[str] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[str] = None
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

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

movie_query = input("Enter your paragraph: ")

final_prompt = prompt_template.invoke(
    {
        "movie_query": movie_query,
        "format_instructions": parser.get_format_instructions()
    }
)

response = model.invoke(final_prompt)

movie = parser.parse(response.content)

print("\n🎬 Movie Information\n")
print(movie.model_dump_json(indent=4))