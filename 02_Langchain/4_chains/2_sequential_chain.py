from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv(override=True)

model=ChatOpenAI(
    model=os.getenv("GROQ_API_MODEL"),
    base_url=os.getenv("GROQ_API_BASE_URL"),
    api_key=os.getenv("GROQ_API_KEY")
)

prompt1=PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({"topic":"Impact of AI to the world"})
print(result)

chain.get_graph().print_ascii()