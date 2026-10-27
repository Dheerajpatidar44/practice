"""
=============================================================================
Phase 1: Pydantic Basics
Topic: Required vs Optional Fields & Default Values
=============================================================================
- Required Field: Jisme koi default value nahi hoti. Agar user pass na kare to error aayega.
- Default Value: Field ke aage = value likh di, user na de to default use hoga.
- Optional Field: Field ho bhi sakti hai aur None bhi (Optional[T] = None ya T | None = None).
"""

from typing import Optional
from pydantic import BaseModel, ValidationError

class UserProfile(BaseModel):
    # 1. REQUIRED FIELDS (Inka dena zaroori hai)
    username: str
    email: str
    
    # 2. DEFAULT VALUES (Agar user na de to default set ho jayega)
    role: str = "customer"
    is_verified: bool = False
    
    # 3. OPTIONAL FIELDS (De bhi sakte hain, aur None bhi ho sakta hai)
    bio: Optional[str] = None
    phone_number: str | None = None  # Python 3.10+ syntax for Optional

print("=" * 60)
print("1. Passing ONLY Required Fields (Defaults will be used)")
print("=" * 60)

u1 = UserProfile(username="dheeraj44", email="dheeraj@example.com")
print("User 1:", u1)
print(f"Role: {u1.role} (default)")
print(f"Bio: {u1.bio} (None)")


print("\n" + "=" * 60)
print("2. Overriding Defaults & Providing Optional Fields")
print("=" * 60)

u2 = UserProfile(
    username="admin_vikram",
    email="vikram@admin.com",
    role="superadmin",
    is_verified=True,
    bio="AI Developer & Python enthusiast",
    phone_number="+91-9876543210"
)
print("User 2:", u2)


print("\n" + "=" * 60)
print("3. Missing a Required Field (ValidationError)")
print("=" * 60)

try:
    # email missing hai, jo ki required field hai!
    u3 = UserProfile(username="incomplete_user")
except ValidationError as e:
    print("Caught Error because 'email' is required:")
    print(e)
