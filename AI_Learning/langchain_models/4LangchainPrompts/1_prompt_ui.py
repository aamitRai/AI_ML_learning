from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Streamlit UI
st.header("LangChain Prompt UI")

paperName = st.selectbox("Select a Paper", options=["Attention is all you need", "GPT-3", "BERT"], key="paper_select")
contentType = st.selectbox("Select a Content Type", options=["Beginner friendly", "Technical", "Mathematical"], key="content_type")
contentLength = st.selectbox("Select a Length", options=["short", "medium", "long"], key="content_length")

# Prompt Template
template = PromptTemplate(
    template="""
    Create a prompt for the paper: {paperName} 
    with content type: {contentType} 
    and length: {contentLength}.
    """,
    input_variables=["paperName", "contentType", "contentLength"]
)

# Generate prompt using user input
prompt = template.invoke({
    'paperName': paperName,
    'contentType': contentType,
    'contentLength': contentLength
})




# On Submit, generate result
if st.button("Submit"):
    result = llm.invoke(prompt)
    st.write("✅ Prompt generated successfully!")
    st.write(f"**LLM Output:**\n\n{result.content}")
