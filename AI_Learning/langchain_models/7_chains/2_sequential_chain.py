from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser

prompt1 =PromptTemplate(
    template="Generate a 1 page report for this topic  {topic} add introduction, body and conclusion with headings",
    input_variables=["topic"]
)
prompt2 =PromptTemplate(
    template="Give me 5 small interesting facts about {text}",
    input_variables=["text"]
)
parser = StrOutputParser()
chain = prompt1 | llm | parser | prompt2 | llm | parser
result = chain.invoke({'topic': 'Love'})
print("result is ",result)
chain.get_graph().print_ascii()
