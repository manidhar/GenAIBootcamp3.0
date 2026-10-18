from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document="Delhi is the capital of India"

docVector=embedding.embed_query(document)

#print(len(docVector))

documents=[
    "Delhi si the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vector=embedding.embed_documents(documents)

print(str(vector))
print(len(vector))

print(vector[0])
print(len(vector[0]))

