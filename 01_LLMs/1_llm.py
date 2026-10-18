from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def get_groq_llm():
    return ChatOpenAI(
        model="openai/gpt-oss-120b",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=1000
    )

llm=get_groq_llm()

result=llm.invoke("write a 5 line poem on cricket")
#print(result)
print(result.content)