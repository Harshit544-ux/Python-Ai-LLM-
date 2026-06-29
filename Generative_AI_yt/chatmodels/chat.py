from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

response = model.invoke("give me a paragraph on machine learning")

print(response.content)