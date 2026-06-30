from langchain_huggingface  import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# load the .env
load_dotenv()

# Hugging Face model
llm = HuggingFaceEndpoint(
    # pass repo id
    repo_id="deepseek-ai/DeepSeek-V4-Pro"
)

model = ChatHuggingFace(llm=llm)

# response 
response = model.invoke("hi how are you")
print(response.content)