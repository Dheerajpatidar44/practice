"""
=============================================================================
Phase 5: Model Configuration
Topic: Field Aliases & populate_by_name
=============================================================================
JavaScript / Frontend APIs aksar camelCase use karti hain (e.g., firstName, userEmail),
lekin Python me PEP-8 standard snake_case hai (e.g., first_name, user_email).
Pydantic ka 'alias' mapping is mismatch ko elegantly solve karta hai:
- Field(alias="camelCaseName"): External key ko Pythonic variable se map karta hai.
- populate_by_name=True: Hum chahein to alias se bhi initialize kar sakte hain
  ya pythonic variable name se bhi!
"""

from pydantic import BaseModel, ConfigDict, Field

class EmployeeRecord(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    # External JSON me "empId" aayega, hum Python me "emp_id" use karenge
    emp_id: int = Field(alias="empId")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    phone_number: str = Field(alias="contactNumber")

print("=" * 60)
print("1. Parsing CamelCase JSON Payload (Using Aliases)")
print("=" * 60)

# Typical Frontend / JavaScript JSON:
frontend_json = {
    "empId": 501,
    "firstName": "Dheeraj",
    "lastName": "Patidar",
    "contactNumber": "+91-9876543210"
}

emp = EmployeeRecord(**frontend_json)
print("Parsed Object:", emp)
# Clean Pythonic access:
print(f"Python Attribute: emp.first_name -> {emp.first_name}")
print(f"Python Attribute: emp.phone_number -> {emp.phone_number}")


print("\n" + "=" * 60)
print("2. Initializing Using Python Names (populate_by_name=True)")
print("=" * 60)

# populate_by_name=True ki wajah se python field names bhi accept honge:
emp2 = EmployeeRecord(
    emp_id=502,
    first_name="Amit",
    last_name="Sharma",
    phone_number="+91-1122334455"
)
print("Initialized with Python names:", emp2)


print("\n" + "=" * 60)
print("3. Exporting with Aliases (Sending back to Frontend)")
print("=" * 60)

# by_alias=True se wapas camelCase me export hoga:
camel_json = emp.model_dump_json(by_alias=True, indent=2)
print("Exported for Frontend (by_alias=True):\n" + camel_json)
