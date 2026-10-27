"""
=============================================================================
Phase 2: Fields & Data Validation
Topic: Cross-Field Validation with @model_validator
=============================================================================
Jab validation ke liye ek se zyada fields ko apas me compare karna ho
(e.g., password == confirm_password, ya start_date < end_date):
- @model_validator(mode='after') use karte hain.
- 'self' ke through poore model ke fields access hote hain.
"""

from datetime import date
from pydantic import BaseModel, model_validator, ValidationError

# Example 1: Password Confirmation
class UserSignup(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def verify_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Password and Confirm Password match nahi ho rahe hain!")
        return self


# Example 2: Date Range Validation
class EventBooking(BaseModel):
    event_name: str
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def verify_date_order(self):
        if self.end_date < self.start_date:
            raise ValueError(f"end_date ({self.end_date}) start_date ({self.start_date}) se pehle nahi ho sakti!")
        return self


print("=" * 60)
print("1. Valid Signup & Booking")
print("=" * 60)

signup = UserSignup(username="dheeraj", password="secretPassword123", confirm_password="secretPassword123")
print("Signup Success:", signup.username)

booking = EventBooking(
    event_name="AI Workshop",
    start_date=date(2026, 11, 1),
    end_date=date(2026, 11, 5)
)
print("Booking Success:", booking.event_name, f"({booking.start_date} to {booking.end_date})")


print("\n" + "=" * 60)
print("2. Testing Cross-Field Errors")
print("=" * 60)

try:
    bad_signup = UserSignup(username="dheeraj", password="password1", confirm_password="password2")
except ValidationError as e:
    print("Caught Password Mismatch Error:")
    for err in e.errors():
        print(f"  - {err['msg']}")

try:
    bad_booking = EventBooking(
        event_name="Hackathon",
        start_date=date(2026, 11, 10),
        end_date=date(2026, 11, 5)  # Invalid: end is before start!
    )
except ValidationError as e:
    print("\nCaught Date Range Error:")
    for err in e.errors():
        print(f"  - {err['msg']}")
