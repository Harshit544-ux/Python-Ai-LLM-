# Zero Shot Prompting

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

# zero shot prompting : Direct giving instructions to the model
SYSTEM_PROMPT = """
 You are a Math Teacher Assistant ,Your name is Harshit ,which expertise in solving math problems.
 if any body ask another questions which is not related to math . Just simply say that sorry I am not able to answer 
 this question because I am a Math Teacher Assistant and I can only answer math related questions.
"""

# Call the chat completion API
response = client.chat.completions.create(
  model="deepseek/deepseek-v4-flash",
  messages=[
        {"role" : "system" , "content" : SYSTEM_PROMPT},
        {"role" : "user" , "content" :"what is the square root of 16 ?"}
        ],

)

# Print the model's response content
print(response.choices[0].message.content)