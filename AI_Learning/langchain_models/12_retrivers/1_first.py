from langchain_community.retrievers import WikipediaRetriever
retrivers=WikipediaRetriever(top_k_results=2,len="en")
query="india pakistan"
docs=retrivers.invoke(query)
print(docs)