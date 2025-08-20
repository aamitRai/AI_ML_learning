from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
prompt1 =PromptTemplate(
    template="Summarize this  {topic}",
    input_variables=["topic"]
)

from langchain_community.document_loaders import TextLoader
loader =TextLoader('cricket.txt', encoding='utf-8')
docs=loader.load()
parser = StrOutputParser()

# print(docs)
# print("\n type is ",type(docs))
# print("\n Number of documents loaded:", len(docs))
# print("\n First document content:", docs[0].page_content)
# print("\n Metadata of first document:", docs[0].metadata)
chain=prompt1 | llm |parser
result =chain.invoke({'topic': docs[0].page_content})
print("result is ",result)
