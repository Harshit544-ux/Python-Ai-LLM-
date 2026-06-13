import os

# Set environment variables to handle macOS fork-safety and multi-threading limitations
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

from dotenv import load_dotenv

load_dotenv()

# Global variables for lazy initialization
_client = None
_vector_store = None

def get_openai_client():
    global _client
    if _client is None:
        from openai import OpenAI
        _client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
    return _client

# vector store for lazy initialization
def get_vector_store():
    global _vector_store
    if _vector_store is None:
        # Import heavy packages inside the helper function to prevent
        # the RQ parent worker process from initializing PyTorch prior to forking.
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_qdrant import QdrantVectorStore
      
        # Load existing Qdrant collection
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        _vector_store = QdrantVectorStore.from_existing_collection(
            url="http://localhost:6333",
            collection_name="learning_rag",
            embedding=embeddings
        )
    return _vector_store

# query processsing
def process_query(query: str):
    print("searching chunks", query)
    
    # Retrieve the vector store lazily within the child process
    vector_store = get_vector_store()
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

    # Retrieve the OpenAI client lazily
    client = get_openai_client()
    response = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )
    print("Response:", response.choices[0].message.content)
    return response.choices[0].message.content