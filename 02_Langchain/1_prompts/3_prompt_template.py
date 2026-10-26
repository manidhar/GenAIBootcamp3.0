from langchain_core.prompts import PromptTemplate
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

template=PromptTemplate(
    template='Greet this person in 5 languages and ensure it have telugu language always Also ensure you use language symantics. The name of the person is {name}',
    input_variables=['name']
)

prompt=template.invoke({'name':'Manidhar'})

llm = get_groq_llm()
result=llm.invoke(prompt)
print(result.content)