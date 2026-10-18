import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
load_dotenv(override=True)

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-0.6B",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)
result=model.invoke("What is the capital of India?")

print(result.content)