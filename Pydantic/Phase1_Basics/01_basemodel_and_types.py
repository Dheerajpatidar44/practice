"""
=============================================================================
Phase 1: Pydantic Basics
Topic: BaseModel, Type Annotations & Basic Data Types
=============================================================================
- BaseModel: Har Pydantic model ka parent class hota hai.
- Type Annotations: Python ke standard types (str, int, float, bool) use hote hain.
- Automatic Coercion: Pydantic strict hone ke sath smart bhi hai, convertible
  types ko automatically target type me convert kar deta hai (e.g., '3.14' -> 3.14).
"""

from pydantic import BaseModel

# 1. Model define karna
class Student(BaseModel):
    id: int               # Integer (e.g., 101)
    name: str             # String (e.g., "Rohit")
    percentage: float     # Float (e.g., 85.5)
    is_active: bool       # Boolean (True / False)

print("=" * 60)
print("1. Creating Model Instance with Perfect Types")
print("=" * 60)

s1 = Student(id=101, name="Rohit Sharma", percentage=89.5, is_active=True)
print("Student 1:", s1)
# Attributes access karna:
print(f"Name: {s1.name}, ID: {s1.id}, Score: {s1.percentage}%")


print("\n" + "=" * 60)
print("2. Automatic Type Coercion (Smart Conversion)")
print("=" * 60)

# Yahan id string me di hai "102", percentage "91.2", is_active "yes" / 1
# Pydantic inko automatically sahi types (int, float, bool) me convert kar deta hai!
s2 = Student(id="102", name="Priya", percentage="91.2", is_active=1)
print("Student 2 (Auto Converted):", s2)
print(f"id type: {type(s2.id)}, is_active type: {type(s2.is_active)}")


print("\n" + "=" * 60)
print("3. Creating Model from a Dictionary (Unpacking **data)")
print("=" * 60)

student_data = {
    "id": 103,
    "name": "Aman",
    "percentage": 78.0,
    "is_active": False
}

s3 = Student(**student_data)
print("Student 3 from dict:", s3)
