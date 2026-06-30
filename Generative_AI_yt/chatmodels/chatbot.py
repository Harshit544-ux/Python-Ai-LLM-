import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

load_dotenv()


print(os.getenv("GOOGLE_API_KEY"))

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    )

# deal with multiple ai mode
print("choose your AI mode")
print("press 1 for angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")

choice = int(input("tell your response :- "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impateintly."
elif choice == 2:
      mode = "You are very funny AI agent. You respond with funny and jokes."
elif choice == 3:
       mode = "You are very sad  AI agent. You respond sadly and heartbreaking"


# maintain the history in list message =[] 
message = [
    SystemMessage(content=mode)
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
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("🤖 Bot : ",response.content)

# print the message
print("messages = " , message)