import os
from openai import OpenAI
from dotenv import load_dotenv # Used to load environment variables from a .env file

# Load environment variables from LLM/.env
load_dotenv()

# Initialize the OpenAI client (configured for OpenRouter)
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"), # Fetch API key from environment
)

# Call the chat completion API
response = client.chat.completions.create(
  model="deepseek/deepseek-v4-flash",
  messages=[
          {
              "role":"system",
              "content":"You are a Doctor Assistant , which expertise in Heart related diseases . "
              "If someone ask you any question which is not related to the Heart related diseases then you will simply say said that sorry I am not able to answer this question"
          },
          {
            "role": "user",
            "content": "what is Arrhythmia? in explain in two lines"
          }
        ],

)

# Print the model's response content
print(response.choices[0].message.content)