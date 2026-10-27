"""
=============================================================================
Phase 5: Model Configuration
Topic: ConfigDict & Handling Extra Fields (ignore, forbid, allow)
=============================================================================
Agar input data me aise fields hon jo hamare Model me defined nahi hain:
- extra='ignore' (Default): Extra fields ko chupchap discard kar deta hai.
- extra='forbid': Strict mode! Agar anjaan field aaya to ValidationError dega.
- extra='allow': Extra fields ko model me accept karke store kar leta hai.
"""

from pydantic import BaseModel, ConfigDict, ValidationError

# 1. Model with extra='ignore' (Default behavior)
class UserIgnoreExtra(BaseModel):
    model_config = ConfigDict(extra="ignore")
    username: str
    email: str

# 2. Model with extra='forbid' (Strict security / APIs)
class UserForbidExtra(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str
    email: str

# 3. Model with extra='allow' (Dynamic fields allow karna)
class UserAllowExtra(BaseModel):
    model_config = ConfigDict(extra="allow")
    username: str
    email: str

raw_payload = {
    "username": "dheeraj",
    "email": "dheeraj@example.com",
    "unknown_token": "xyz_12345",   # EXTRA FIELD!
    "hacker_field": True            # EXTRA FIELD!
}

print("=" * 60)
print("1. extra='ignore' (Extra fields discarded)")
print("=" * 60)
u_ignore = UserIgnoreExtra(**raw_payload)
print("Result:", u_ignore)
print("Extra fields discarded cleanly.")


print("\n" + "=" * 60)
print("2. extra='forbid' (Raises ValidationError on unexpected fields)")
print("=" * 60)
try:
    u_forbid = UserForbidExtra(**raw_payload)
except ValidationError as e:
    print("Caught Strict Forbid Error:")
    for err in e.errors():
        print(f"  - Unexpected field: {err['loc'][0]} ({err['msg']})")


print("\n" + "=" * 60)
print("3. extra='allow' (Extra fields accepted and accessible)")
print("=" * 60)
u_allow = UserAllowExtra(**raw_payload)
print("Result:", u_allow)
print("Accessible extra field:", getattr(u_allow, "unknown_token"))
