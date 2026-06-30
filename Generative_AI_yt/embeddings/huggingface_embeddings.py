from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts=[
    'Hello this is Harshit',
    'Im from Hyderabad',
    'Working as a Software Engineer'
]

vector = embeddings.embed_documents(texts)
print(vector)
print(len(vector))
