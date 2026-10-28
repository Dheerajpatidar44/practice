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
