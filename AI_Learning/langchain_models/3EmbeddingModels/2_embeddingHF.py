from langchain_huggingface import HuggingFaceEmbeddings
embeddding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
text= "capital of india"
vector=embeddding.embed_query(text)
print(str(vector))