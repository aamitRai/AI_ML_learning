from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

loader =TextLoader('cricket.txt', encoding='utf-8')
docs=loader.load()

splitter= CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=2,
    separator="\n"
)
result=splitter.split_text(docs[0].page_content)
print(result)