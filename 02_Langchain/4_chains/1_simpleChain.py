from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv(override=True)

def getGrooqModel():
    return ChatOpenAI(
        model=os.getenv("GROQ_API_MODEL"),
                        base_url=os.getenv("GROQ_API_BASE_URL"),
                        api_key=os.getenv("GROQ_API_KEY")
    )

prompt=PromptTemplate(
    template="Genearate 5 interesting facts about {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()
model=getGrooqModel()
chain=prompt | model | parser
result=chain.invoke({'topic':'cricket'})
print(result)
chain.get_graph().print_ascii()

