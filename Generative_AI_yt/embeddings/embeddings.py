from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model='text-embeddings-3-large',
    dimensions=64
)

texts=[
    'Hello this is Harshit',
    'Im from Hyderabad',
    'Working as a Software Engineer'
]

vector = embeddings.aembed_documents(texts)
print(vector)