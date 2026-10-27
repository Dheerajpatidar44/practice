# def insert_patient_data(name: str, age: int):

#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError('Incorrect age')
#         else:
#             print(name)
#             print(age)
#             print('inserted to database ')
#     else: 
#         raise TypeError('Incorrect data types')

# def update_patient_data(name: str, age: int):

#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
#         print('updated to database ')
#     else: 
#         raise TypeError('Incorrect data types')

# insert_patient_data('dheeraj', 30)

# ye problem aati he pyhton me type validation ke liye 
# isko solve karne ke liye hum pydantic ka use krte he 

from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
   
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info={'name': 'dheeraj', 'age': 30, 'weight':75.5, 'married':True, 'allergies':['dust', 'pollen'], 'contact_details':{'email':'dheeraj@gmail.com', 'phone':'1234567890'}} 
    
patient1 = Patient(**patient_info)
insert_patient_data(patient1)

