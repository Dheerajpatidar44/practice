"""
=============================================================================
Phase 4: Model Serialization & Deserialization
Topic: Exporting Models with model_dump() and model_dump_json()
=============================================================================
Pydantic V2 me data export karne ke do primary methods hain:
- model.model_dump(): Model ko Python DICTIONARY me convert karta hai.
- model.model_dump_json(): Model ko JSON STRING me convert karta hai.
- include/exclude: Specific fields ko export me shamil ya hatane ke liye.
- exclude_unset: Sirf un fields ko export karta hai jo user ne explicitly set kiye hon.
"""

from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str                  # Sensitive field!
    bio: Optional[str] = "Default Bio"
    is_active: bool = True

user = User(
    id=1,
    name="Dheeraj Patidar",
    email="dheeraj@example.com",
    password_hash="argon2$secret$hash$12345"
)

print("=" * 60)
print("1. model_dump() -> Python Dictionary")
print("=" * 60)

user_dict = user.model_dump()
print("Type:", type(user_dict))
print("Dict:", user_dict)


print("\n" + "=" * 60)
print("2. model_dump_json() -> Valid JSON String")
print("=" * 60)

user_json = user.model_dump_json(indent=2)
print("Type:", type(user_json))
print("JSON Output:\n" + user_json)


print("\n" + "=" * 60)
print("3. Excluding Sensitive Fields (e.g., password_hash)")
print("=" * 60)

# API response bhejte waqt sensitive field hide karna:
safe_dict = user.model_dump(exclude={"password_hash"})
print("Safe Dict (Without Password):", safe_dict)


print("\n" + "=" * 60)
print("4. Including Only Specific Fields")
print("=" * 60)

minimal_dict = user.model_dump(include={"id", "name"})
print("Minimal Dict:", minimal_dict)


print("\n" + "=" * 60)
print("5. exclude_unset=True (Sirf user dwara di gayi fields)")
print("=" * 60)

# bio aur is_active humne provide nahi kiye the (wo defaults the)
# exclude_unset=True unko chhod dega:
unset_dict = user.model_dump(exclude_unset=True)
print("Explicitly Set Fields Only:", unset_dict)
