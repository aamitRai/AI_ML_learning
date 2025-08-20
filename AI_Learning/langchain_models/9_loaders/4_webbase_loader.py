from langchain_community.document_loaders import WebBaseLoader
url='https://aetheriustechnologies.com/'
urls = [
    "https://aetheriustechnologies.com/",
    "https://aetheriustechnologies.com/about",
    "https://aetheriustechnologies.com/services",
    # Add more discovered pages...
]
loader = WebBaseLoader(urls)
docs = loader.load()   
print("\nNumber of documents loaded:", len(docs))
print("metadata of first document:", docs[0].metadata)  
print("docs[0].page_content[:500])  ",docs[0].page_content) 
print("docs[0].page_content[:500])  ",docs[1].page_content) 
print("docs[0].page_content[:500])  ",docs[2].page_content) 
