from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
import os

load_dotenv(override=True)

def get_grooqLLM():
    return ChatOpenAI(
         model=os.getenv("GROQ_API_MODEL"),
                base_url=os.getenv("GROQ_API_BASE_URL"),
                api_key=os.getenv("GROQ_API_KEY")
    )

model=get_grooqLLM()

class Person(BaseModel):
    name:str=Field(description="Name of the person")
    city:str=Field(description="Name of the city the person belongs to")
    age:int=Field(gt=18,description="Age of the person")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

print(template.template)

chain=template | model | parser

final_result=chain.invoke({'place':'India'})
print(final_result)