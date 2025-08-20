from langchain_chroma import Chroma  
from langchain.schema import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style.",
    metadata={"team": "Royal Challengers Bangalore"}
)

doc2 = Document(
    page_content="Rohit Sharma is the most successful captain and batsmen in IPL history, leading Mumbai Indians to five titles. He's known for his calm leadership.",
    metadata={"team": "Mumbai Indians"}
)

doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicket-keeping, and leadership are unmatched.",
    metadata={"team": "Chennai Super Kings"}
)
vector_store = Chroma(
    persist_directory="chroma_db",
    collection_name="ipl_players_2025_1",
    embedding_function=embedding,
)
vector_store.add_documents([doc2, doc1, doc3])
retrievers = vector_store.as_retriever(search_kwargs={"k": 3})

result=retrievers.invoke("batsman")
print("result",result)