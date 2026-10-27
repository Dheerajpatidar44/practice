"""
=============================================================================
Phase 2: Fields & Data Validation
Topic: Custom Single-Field Validation with @field_validator
=============================================================================
Jab built-in constraints kaafi na hon aur custom logic lagana ho:
- @field_validator('field_name') decorator use karte hain.
- Function me @classmethod lagta hai.
- Value validate bhi hoti hai aur modify/clean (transformation) bhi kar sakte hain.
"""

from pydantic import BaseModel, field_validator, ValidationError

class Employee(BaseModel):
    name: str
    email: str
    pan_card: str

    # 1. Name validator: Pehla letter capital karna aur extra spaces hatana
    @field_validator("name")
    @classmethod
    def clean_name(cls, value: str) -> str:
        cleaned = value.strip().title()
        if len(cleaned) < 2:
            raise ValueError("Name kam se kam 2 characters ka hona chahiye")
        return cleaned

    # 2. Email validator: Domain check karna
    @field_validator("email")
    @classmethod
    def validate_corporate_email(cls, value: str) -> str:
        value = value.strip().lower()
        if "@" not in value or not value.endswith(".com"):
            raise ValueError("Email valid format me honi chahiye aur '.com' par end honi chahiye")
        return value

    # 3. PAN card validator: Exact 10 characters aur uppercase
    @field_validator("pan_card")
    @classmethod
    def validate_pan(cls, value: str) -> str:
        value = value.strip().upper()
        if len(value) != 10 or not value.isalnum():
            raise ValueError("PAN Card exact 10 alphanumeric characters ka hona chahiye (e.g. ABCDE1234F)")
        return value

print("=" * 60)
print("1. Valid Employee (With Automatic Data Cleaning)")
print("=" * 60)

# Notice: naam me lowercase/extra spaces, email me spaces, PAN me lowercase
emp1 = Employee(
    name="   dheeraj patidar   ",
    email=" DHEERAJ@company.COM ",
    pan_card="abcde1234f"
)

print("Employee 1 (Auto cleaned):", emp1)
print(f"Cleaned Name: '{emp1.name}'")
print(f"Cleaned Email: '{emp1.email}'")
print(f"Upper PAN: '{emp1.pan_card}'")


print("\n" + "=" * 60)
print("2. Invalid Data Triggering Custom Errors")
print("=" * 60)

try:
    emp2 = Employee(
        name="A",
        email="invalid_email_format",
        pan_card="TOO_SHORT"
    )
except ValidationError as e:
    print("Caught Custom Field Validation Errors:")
    for err in e.errors():
        print(f"  - {err['loc'][0]}: {err['msg']}")
