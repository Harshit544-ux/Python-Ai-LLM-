import os
from dotenv import load_dotenv # Used to load environment variables from a .env file
from google import genai

# Load environment variables from LLM/.env
load_dotenv()

# Initialize the Gemini client using the API key from the environment
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Generate content using the specified model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="what is llm"
)

# Print the model's response
print(response.text)