from typing import TypedDict

class Person(TypedDict):
    name: str
    age:int

new_person: Person={'name':'Manidhar','age':'44'}
print(new_person)
print(type(new_person))