from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
template1 = PromptTemplate(
    template="What is the {topic} and its detail?",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template="Summarize this in 5 points: {text}",
    input_variables=["text"]
)
parser = StrOutputParser()
chain = template1 | llm| parser |template2 | llm|parser
result=chain.invoke({'topic': 'Manifestation'})
print("\n ", result)