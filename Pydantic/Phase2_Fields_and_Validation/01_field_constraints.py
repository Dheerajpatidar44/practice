"""
=============================================================================
Phase 2: Fields & Data Validation
Topic: Field() & Built-in Constraints
=============================================================================
Field() function se hum fields ke upar strict constraints laga sakte hain:
- Numbers ke liye: gt (greater than), ge (greater/equal), lt (less than), le (less/equal)
- Strings ke liye: min_length, max_length, pattern (regex)
- Documentation: description, examples
"""

from pydantic import BaseModel, Field, ValidationError

class Product(BaseModel):
    # String constraints
    title: str = Field(
        ...,                    # ... (Ellipsis) ka matlab hai ye field REQUIRED hai
        min_length=3,
        max_length=50,
        description="Product ka naam, 3 se 50 characters ke beech hona chahiye"
    )
    
    # Numeric constraints
    price: float = Field(
        ...,
        gt=0,                   # price must be greater than 0
        description="Price 0 se zyada honi chahiye"
    )
    
    discount_percentage: float = Field(
        default=0.0,
        ge=0,                   # greater than or equal to 0
        le=100,                 # less than or equal to 100
        description="Discount 0 se 100% ke beech ho sakta hai"
    )
    
    stock: int = Field(
        default=1,
        ge=0,
        description="Stock negative nahi ho sakta"
    )

print("=" * 60)
print("1. Valid Product Instance")
print("=" * 60)

p1 = Product(title="Wireless Mouse", price=799.0, discount_percentage=10.0, stock=50)
print("Product 1:", p1)


print("\n" + "=" * 60)
print("2. Testing Invalid Constraints")
print("=" * 60)

# Invalid: price is -50 and title is too short ("A")
try:
    p2 = Product(title="A", price=-50.0, discount_percentage=150.0)
except ValidationError as e:
    print("Caught Constraints Violations:")
    for err in e.errors():
        field_name = err["loc"][0]
        message = err["msg"]
        print(f"  - Field '{field_name}': {message}")
