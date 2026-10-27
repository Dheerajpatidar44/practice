"""
=============================================================================
Phase 7: Pydantic with FastAPI
Topic: Request Models, Response Models & Automatic Validation Errors
=============================================================================
FastAPI ka core engine Pydantic par bana hai:
1. Request Body Model: Incoming JSON data ko parse & validate karta hai.
2. Response Model: Outgoing response ko shape karta hai (sensitive data jaise password hide karta hai).
3. Automatic 422: Agar client galat data bheje, to FastAPI bina kisi extra code ke
   HTTP 422 Unprocessable Entity error return kar deta hai.
"""

from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Pydantic + FastAPI Demo")

# 1. REQUEST MODEL (Client se aane wala data)
class UserCreateRequest(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$", description="Valid email address")
    password: str = Field(min_length=6, description="Plain text password (never return this!)")
    age: int = Field(ge=18, le=120)

# 2. RESPONSE MODEL (Client ko wapas bhejne wala data - Notice: password is excluded!)
class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    age: int
    is_active: bool = True

# In-memory database simulation
user_database = []

# 3. FASTAPI ROUTE
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreateRequest):
    # Pydantic has already validated payload here!
    new_id = len(user_database) + 1
    
    # User ko DB me save kiya:
    user_record = {
        "user_id": new_id,
        "username": payload.username,
        "email": payload.email,
        "password_hash": f"hashed_{payload.password}",
        "age": payload.age,
        "is_active": True
    }
    user_database.append(user_record)
    
    # Response model automatically filters out password_hash!
    return user_record


# ---------------------------------------------------------------------------
# Test Execution using FastAPI TestClient (Runs immediately in terminal!)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    client = TestClient(app)

    print("=" * 60)
    print("1. Sending VALID Request to FastAPI (HTTP 201 Expected)")
    print("=" * 60)

    valid_payload = {
        "username": "dheeraj_dev",
        "email": "dheeraj@gmail.com",
        "password": "superSecret123",
        "age": 24
    }

    response = client.post("/users", json=valid_payload)
    print(f"Status Code : {response.status_code}")
    print(f"Response Body: {response.json()}")
    print("Notice: 'password' response me bilkul nahi hai (Response Model filtered it!)")


    print("\n" + "=" * 60)
    print("2. Sending INVALID Request to FastAPI (HTTP 422 Automatic Error)")
    print("=" * 60)

    invalid_payload = {
        "username": "ab",                # Error: length < 3
        "email": "not-an-email",         # Error: invalid pattern
        "password": "123",               # Error: length < 6
        "age": 14                        # Error: age < 18
    }

    bad_response = client.post("/users", json=invalid_payload)
    print(f"Status Code : {bad_response.status_code} (Unprocessable Entity)")
    print("FastAPI Automatic Error Breakdown:")
    for err in bad_response.json()["detail"]:
        field = err["loc"][-1]
        msg = err["msg"]
        print(f"  - Field '{field}': {msg}")
