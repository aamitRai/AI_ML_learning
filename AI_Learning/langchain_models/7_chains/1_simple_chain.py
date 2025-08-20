from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser

prompt =PromptTemplate(
    template="Give me 5 small interesting facts about {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()
chain = prompt | llm | parser
result = chain.invoke({'topic': 'Love'})
print("result is ",result)
chain.get_graph().print_ascii()
