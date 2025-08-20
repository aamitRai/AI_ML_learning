from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.schema import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma  
from langchain.schema import Document
from langchain_google_genai import ChatGoogleGenerativeAI


# Step 1: Initialize embedding model
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Step 2: Create documents (replace with your actual documents)
all_docs = [
    Document(page_content="Exercise boosts energy and improves overall wellness."),
    Document(page_content="Balanced diets and hydration are key to maintaining energy."),
    Document(page_content="Meditation and rest are crucial for mental balance."),
    Document(page_content="Getting enough sleep can improve energy levels."),
    Document(page_content="Avoid burnout by pacing work and prioritizing recovery."),
]

vectorstore = Chroma(
    persist_directory="chroma_db",
    collection_name="ipl_players_2025_1",
    embedding_function=embedding,
)


# Step 4: Create standard and multi-query retrievers
similarity_retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
)

# Step 5: Query
query = "How to improve energy levels and maintain balance?"

# Step 6: Retrieve results
similarity_results = similarity_retriever.invoke(query)
multiquery_results = multiquery_retriever.invoke(query)

# Step 7: Print comparison
print("\n--- Similarity Retriever Results ---")
for i, doc in enumerate(similarity_results):
    print(f"\nResult {i+1}:\n{doc.page_content}")

print("\n--- MultiQuery Retriever Results ---")
for i, doc in enumerate(multiquery_results):
    print(f"\nResult {i+1}:\n{doc.page_content}")
