from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
student_info ="""
    Amit Sharma is a 2020 B.Tech passout student specializing in Computer Science at the National Institute of Technology. At 20 years old, he has demonstrated strong academic performance with a current GPA of 8.5. he has 2 year expereince in it , Amit is passionate about software development and has developed skills in Python, C++, data structures, and web development. He is actively involved in coding competitions and has completed several personal projects. Known for his problem-solving abilities and teamwork, Amit continues to seek opportunities to apply his knowledge in real-world applications. He is currently open to internships where he can contribute to innovative tech solutions while gaining industry experience.
    """
schema={
    "title":"student",
    "description":"schema for student",
    "type":"object",
    "properties":{  
        "name":{
            "type":"string",
            "description":"name of the student"
        },
        "age":{
            "type":"integer",
            "description":"age of the student"
        }
    },
    "required":["name","age"]

}

structured_model=llm.with_structured_output(schema)
result = structured_model.invoke(student_info)
print("\n ",result)