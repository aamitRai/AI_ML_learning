from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

prompt1 =PromptTemplate(
    template="Give me  interesting joke {topic}",
    input_variables=["topic"]
)
prompt2 =PromptTemplate(
    template="explain this joke in 5  line {joke} ,include joke along with explanation",
    input_variables=["joke"]
)
parser = StrOutputParser()
chain=RunnableSequence(prompt1 , llm , prompt2,prompt2, llm,parser)
result = chain.invoke({'topic': 'Love'})
print("result is ",result)
chain.get_graph().print_ascii()
