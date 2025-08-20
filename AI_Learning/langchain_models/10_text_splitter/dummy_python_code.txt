from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

user: User = {
    "name": "Alice",
    "age": 30
}
def greet_user(user: User) -> str:
    return f"Hello, {user['name']}! You are {user['age']} years old."

print(greet_user({"name": "Amit", "age": 25}))