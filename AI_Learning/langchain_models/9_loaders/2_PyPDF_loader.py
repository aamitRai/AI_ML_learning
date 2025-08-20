from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

loader =PyPDFLoader('resume_amit.pdf')
docs=loader.load()
print("\n Number of documents loaded:", len(docs))
print("\n First document content:", docs[0].page_content)