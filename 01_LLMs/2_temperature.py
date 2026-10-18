from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv(override=True)

def get_groq_llm():
    return ChatOpenAI(
        model=os.getenv("GROQ_API_MODEL"),
        base_url=os.getenv("GROQ_API_BASE_URL"),
        api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=1000,
        temperature=0.7,
        top_p=0.9
    )

model=get_groq_llm()

result=model.invoke("write a 5 line poem on cricket")
#print(result)
print(result.content)