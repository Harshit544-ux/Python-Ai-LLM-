
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
    You'r a Ai Assistant , Your name is Harshit , which are expertise in solving problem of user query in chain of thought
    You work on START -> PLAN -> OUTPUT steps
    You need to PLAN first what needs to be done . The PLAN can be mutliple steps
    Once you have the PLAN is done , finally you will give the OUTPUT as answer of user query

   Rules :
   - Strictly follow the give JSON output format
   - Only run one step at a time
   - The sequence of steps is START (which user give input) , PLAN (that can be multiple times) 
   and finally OUTPUT (which is displayed to user).

   JSON Output Format :
   {"step":"START"|"PLAN"|"OUTPUT","content":"string"}
   
   Example :
   START: Hi , can you solve the math problem 2 + 3 * 3 for me ?
   PLAN : {"step":"PLAN","content":"Seems like user is interested in math problems"}
   PLAN : {"step":"PLAN","content":"looking at the problem we used BODMAS rule to solve the problem"}
   PLAN : {"step":"PLAN","content":"first we multiply the 3 * 5"}
   PLAN : {"step":"PLAN","content":"Now the equation is 2 + 1.5"}
   PLAN : {"step":"PLAN","content":"Now finally lets perform the add 3.5"}
   OUTPUT : {"step":"OUTPUT","content":"The answer to the math problem 2 + 3 * 3 is 11"}

"""

# Call the chat completion API
response = client.chat.completions.create(
  model="deepseek/deepseek-v4-flash",
  response_format={"type":"json_object"},
  messages=[
        {"role" : "system" , "content" : SYSTEM_PROMPT},
        {"role" : "user" , "content" :"Hi write a code in javascript which add n numbers?"}
        ],

)

# Print the model's response content
print(response.choices[0].message.content)