"""
=============================================================================
Phase 0: Getting Ready for Pydantic
Topic: Why Data Validation Matters & Introduction to Pydantic
=============================================================================
Kyu chahiye Pydantic?
Python dynamically typed language hai. Agar kisi function me age: int likha
bhi ho, to Python runtime par koi error nahi deta agar aap 'thirty' bhej do.
Pydantic data parsing aur runtime type validation provide karta hai.
"""

from pydantic import BaseModel, ValidationError

print("=" * 60)
print("1. Problem with Plain Python (No Validation)")
print("=" * 60)

# Plain Python function
def insert_patient_manual(name: str, age: int):
    # Python runtime par type check nahi karta!
    print(f"Saving to DB -> Name: {name} (type: {type(name).__name__}), Age: {age} (type: {type(age).__name__})")

# Dekho: age me 'thirty' (string) pass ho gaya aur Python ne koi error nahi diya!
insert_patient_manual("Amit", "thirty")  # BAD DATA enters database!


print("\n" + "=" * 60)
print("2. The Pydantic Solution (Automatic Validation & Parsing)")
print("=" * 60)

# Pydantic Model
class Patient(BaseModel):
    name: str
    age: int  # Must be an integer or convertible to int

# Case A: Valid Data
p1 = Patient(name="Amit", age=28)
print("Case A (Valid):", p1)

# Case B: Automatic Type Coercion (String number '25' ko int me convert kar dega)
p2 = Patient(name="Rahul", age="25")
print("Case B (Auto Coerced '25' -> int):", p2, "| Type of age:", type(p2.age))

# Case C: Invalid Data ('thirty' cannot be converted to int -> raises ValidationError)
print("\nCase C (Invalid Data Handling):")
try:
    p3 = Patient(name="Amit", age="thirty")
except ValidationError as e:
    print("Caught ValidationError successfully!")
    print(e)
