# Few Shot Prompting

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

# few shot prompting : Direct giving instructions to the model and give some example
SYSTEM_PROMPT = """
 You are a Coding Assistant ,Your name is Alexa ,which expertise in solving coding related problems.
 if any body ask another questions which is not related to coding . Just simply say that sorry I am not able to answer 
 this question

 
Examples :
Q:Can you explain me the a + b of whole square ?
A:Sorry,I'm only able to answer coding related questions.

Q:Hey write the code in python to add two numbers ?
A: def add (a,b):
        return a + b

"""

# Call the chat completion API
response = client.chat.completions.create(
  model="deepseek/deepseek-v4-flash",
  messages=[
        {"role" : "system" , "content" : SYSTEM_PROMPT},
        {"role" : "user" , "content" :"what is python?"}
        ],

)

# Print the model's response content
print(response.choices[0].message.content)