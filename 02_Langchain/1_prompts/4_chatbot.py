from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def get_groq_llm():
    return ChatOpenAI(
        model=os.getenv("GROQ_API_MODEL"),
        base_url=os.getenv("GROQ_API_BASE_URL"),
        api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=1000
    )

llm=get_groq_llm()

chat_history=[
    SystemMessage(content="You are helpful AI Assistant")
]

while True:
    user_input=input('You :  ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    response=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI : ",response.content)

print(chat_history)