"""
=============================================================================
Phase 2: Fields & Data Validation
Topic: Catching & Inspecting Validation Errors
=============================================================================
Jab user galat data deta hai to Pydantic ValidationError raise karta hai.
Hum is error ko catch karke client/user ko clean, readable messages de sakte hain:
- e.errors(): List of dictionary, jisme har error ki details hoti hain.
- e.error_count(): Total kitne errors aaye.
"""

from pydantic import BaseModel, Field, ValidationError

class UserRegistration(BaseModel):
    username: str = Field(min_length=3)
    age: int = Field(ge=18, le=100)
    email: str

print("=" * 60)
print("Testing with Multiple Invalid Fields")
print("=" * 60)

invalid_data = {
    "username": "ab",       # Error: kam se kam 3 characters chahiye
    "age": 15,              # Error: age >= 18 honi chahiye
    # email field bilkul missing hai! (Error: Field required)
}

try:
    user = UserRegistration(**invalid_data)
except ValidationError as e:
    print(f"Total Errors Found: {e.error_count()}\n")

    print("--- 1. Iterating Over Each Error (e.errors()) ---")
    for index, err in enumerate(e.errors(), start=1):
        field = " -> ".join(str(loc) for loc in err["loc"])
        message = err["msg"]
        err_type = err["type"]
        input_value = err.get("input", "<missing>")
        
        print(f"Error #{index}:")
        print(f"  Field   : {field}")
        print(f"  Message : {message}")
        print(f"  Type    : {err_type}")
        print(f"  Input   : {input_value}")
        print("-" * 40)

    print("\n--- 2. Direct Formatted Print ---")
    print(e)
