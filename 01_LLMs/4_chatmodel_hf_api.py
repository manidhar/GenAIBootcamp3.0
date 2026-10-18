import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
load_dotenv(override=True)

# 1. Spin up a local pipeline instead of an external API Endpoint
llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 512, "do_sample": False}
)

# 2. Wrapping local pipelines in ChatHuggingFace is 100% stable
model = ChatHuggingFace(llm=llm)

messages = [
    ("system", "You are a helpful assistant."),
    ("human", "What is the capital of India?"),
]

result = model.invoke(messages)
print(result.content)