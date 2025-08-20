from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence ,RunnablePassthrough,RunnableLambda

prompt1 =PromptTemplate(
    template="Give me  interesting joke {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()
def word_counter(text):
    return len(text.split())

joke_gen_chain = RunnableSequence(prompt1 , llm , parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
   'explaination':  RunnableLambda(word_counter)
})
chain=RunnableSequence(joke_gen_chain, parallel_chain)
result = chain.invoke({'topic': 'Love'})
print("result is ",result)
chain.get_graph().print_ascii()
