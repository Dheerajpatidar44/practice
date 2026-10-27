"""
=============================================================================
Phase 3: Lists, Dictionaries & Nested Models
Topic: Nested Models (Models Inside Models)
=============================================================================
Real-world data often hierarchical hota hai. Jaise ek User ke andar
uska Address ho sakta hai, jo khud ek alag structure hai.
Pydantic me hum ek BaseModel ko dusre BaseModel ke field type ki tarah use karte hain.
"""

from typing import Optional
from pydantic import BaseModel, Field, ValidationError

# 1. Child Model (Address)
class Address(BaseModel):
    street: str
    city: str
    state: str
    pincode: str = Field(min_length=6, max_length=6, description="6 digit pincode")

# 2. Parent Model (Customer)
class Customer(BaseModel):
    id: int
    name: str
    email: str
    address: Address  # Nested Model!
    billing_address: Optional[Address] = None  # Optional Nested Model

print("=" * 60)
print("1. Creating Nested Models from Nested Dictionary")
print("=" * 60)

customer_json = {
    "id": 1001,
    "name": "Dheeraj Patidar",
    "email": "dheeraj@example.com",
    "address": {
        "street": "MG Road, Flat 402",
        "city": "Indore",
        "state": "Madhya Pradesh",
        "pincode": "452001"
    }
}

# Pydantic nested dictionary ko automatically Address model me convert kar dega!
customer = Customer(**customer_json)
print("Customer:", customer)

# Nested fields access karna:
print(f"\nCustomer Name : {customer.name}")
print(f"City          : {customer.address.city}")
print(f"Pincode       : {customer.address.pincode}")


print("\n" + "=" * 60)
print("2. Validation Inside Nested Model")
print("=" * 60)

# Yahan pincode 6 digits se chhota hai ("123") -> Address validate fail karega!
bad_json = {
    "id": 1002,
    "name": "Amit",
    "email": "amit@test.com",
    "address": {
        "street": "Main Road",
        "city": "Bhopal",
        "state": "MP",
        "pincode": "123"  # INVALID!
    }
}

try:
    bad_customer = Customer(**bad_json)
except ValidationError as e:
    print("Caught Nested Error:")
    for err in e.errors():
        # loc will show: ('address', 'pincode')
        field_path = " -> ".join(str(loc) for loc in err["loc"])
        print(f"  Field '{field_path}': {err['msg']}")
