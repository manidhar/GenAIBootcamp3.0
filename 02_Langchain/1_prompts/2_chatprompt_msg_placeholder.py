from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv

import sys
from importlib import import_module
from pathlib import Path

load_dotenv(override=True)

# The lesson filename starts with a digit, so load it by its module path.
# Find the repository root so this works even when launched from this folder.
project_root = Path(__file__).resolve().parents[2]
# Make the repository root available for imports from other lesson folders.
sys.path.insert(0, str(project_root))
get_groq_llm = import_module("01_LLMs.1_llm").get_groq_llm

# chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

#print(chat_history)

# create prompt
prompt=chat_template.invoke({'chat_history':chat_history,'query':'where is my refund?'})

llm = get_groq_llm()

result=llm.invoke(prompt)
print(prompt)
print('---------------------------------------------')
print(result.content)
