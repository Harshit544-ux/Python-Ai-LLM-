from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    )

# maintain the history in list message =[] 
message = [
    SystemMessage(content='You are a funny AI')
]

# welcome message
print("-------Welcome to Harshit Chat Application--------")

# infinite loop
while True:
    prompt = input("😃 You : ")
    message.append(HumanMessage(content=prompt))
    # condition 
    if prompt.lower() in ['exit','quit','byt']:
        print("👋🏻Goodbye !")
        break
    # response 
    response = model.invoke(prompt)
    message.append(AIMessage(content=response.content))
    print("🤖 Bot : ",response.content)

print("messages = " , message)