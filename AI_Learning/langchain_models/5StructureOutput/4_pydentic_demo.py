from pydantic import BaseModel,Field
from typing import Optional
class Student(BaseModel):
    name: str
    age: Optional[int] = None  # Optional field
    grade: str
    cgpa: float=Field(gt=0,lt=10,description="CGPA must be between 0 and 10")

student=Student(name="Amit", grade="A",cgpa=8.5)
print("student:", dict(student)  )
