from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

loader =TextLoader('dummy_python_code.txt', encoding='utf-8')
docs=loader.load()

splitter= RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=2
)
result=splitter.split_text(docs[0].page_content)
print(result)