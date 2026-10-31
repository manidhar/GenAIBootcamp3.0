from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import JsonOutputParser

load_dotenv(override=True)

def get_grooq_llm():
    return ChatOpenAI(
        model=os.getenv("GROQ_API_MODEL"),
        base_url=os.getenv("GROQ_API_BASE_URL"),
        api_key=os.getenv("GROQ_API_KEY")
    )

model=get_grooq_llm()
parser=JsonOutputParser()
template=PromptTemplate(
    template='Give me 5 facts about  {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

parser=JsonOutputParser()

# LCEL - Langchain expression language - syntax (Ex : squencial chain)
chain=template | model | parser
result=chain.invoke({'topic':'black hole'})
print(result)
