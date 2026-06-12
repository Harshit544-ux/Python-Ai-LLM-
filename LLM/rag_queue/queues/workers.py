from openai import OpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing Qdrant collection
vector_store = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embeddings
)

def process_query(query: str):
    print("searching chunks", query)
    search_results = vector_store.similarity_search(query=query, k=4)
    context = "\n\n".join([
        f"Page {doc.metadata.get('page', 'N/A')}:\n{doc.page_content}"
        for doc in search_results
    ])
    SYSTEM_PROMPT = f"""
    You are a helpful assistant who answers questions based on the following context 
    retrieved from a PDF, along with page numbers.

    Only answer based on the context below. If the answer is not in the context, 
    say "I couldn't find this in the document." Also mention the page number 
    where the user can read more.

    Context:
    {context}
    """

    response = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )
    print("Response:", response.choices[0].message.content)
    return response.choices[0].message.content