from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

loader = DirectoryLoader(".", glob="**/*.py", loader_cls=TextLoader)
docs = loader.load()

print("\nNumber of documents loaded:", len(docs))
print("metadata of first document:", docs[0].metadata)
# print("\nFirst document content:\n", docs[0].page_content)
