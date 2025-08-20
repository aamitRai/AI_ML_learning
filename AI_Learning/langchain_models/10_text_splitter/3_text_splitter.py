from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader =TextLoader('dummy_text.txt', encoding='utf-8')
docs=loader.load()

splitter= RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=2
)
result=splitter.split_text(docs[0].page_content)
print(result)