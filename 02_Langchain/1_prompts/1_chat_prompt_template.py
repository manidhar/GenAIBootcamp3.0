from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate(
    [
        ('system','you are helpful {domain} expert'),
        ('human','Explain in simple terms, what is {topic}')
    ]
)

# system message - system prompt
#  human message - user prompt
# ai message - model response
# tool message - tool response

prompt=chat_template.invoke({'domain':'cricket','topic':'no ball'})
print(prompt)