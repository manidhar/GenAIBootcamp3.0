from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

def get_grooq_llm():
    return ChatOpenAI(
        model=os.getenv("GROQ_API_MODEL"),
        base_url=os.getenv("GROQ_API_BASE_URL"),
        api_key=os.getenv("GROQ_API_KEY")
    )

model=get_grooq_llm()

# 1st prompt -> detailed report
template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

#2nd prompt -> summary
template2=PromptTemplate(
    template='write a 5 line summary on the following report. /n {report}',
    input_variables=['report']
)

parser=StrOutputParser()

# LCEL - Langchain expression language - syntax (Ex : squencial chain)
chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'black hole'})
print(result)
