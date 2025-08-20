from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain

prompt =PromptTemplate(
    template="Give me 5 small interesting facts about {topic}",
    input_variables=["topic"]
)
chain=LLMChain(llm=llm, prompt=prompt)

parser = StrOutputParser()
result = chain.run({'topic': 'Love'})
print("result is ",result)
chain.get_graph().print_ascii()
