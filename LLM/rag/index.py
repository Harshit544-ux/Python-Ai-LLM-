from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters  import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv


load_dotenv()

pdf_path = Path(__file__).parent / "Nodejs.pdf"

# Load this file in python program
loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

print(docs[12])

# Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(documents=docs)

# vector embedding
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = QdrantVectorStore.from_documents(
    documents = chunks,
    embedding = embeddings,
    url="http://localhost:6333",
    collection_name="learning_rag",
    force_recreate=True
)

print("Indexing of documents is done....")