from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Manidhar'
    age: Optional[int]=None
    email:EmailStr
    cgpa: float=Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa')

new_student={'age':'44','email':'abce@gmail.com'}
student=Student(**new_student)

print(student)
print(type(student))
student_dict=dict(student)
print(type(student_dict))
student_json=student.model_dump_json()
print(student_json)