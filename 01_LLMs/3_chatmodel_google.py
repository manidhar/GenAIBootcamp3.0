import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)

model=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)

result=model.invoke("What is the capital of India")
print(result.content[0]["text"])