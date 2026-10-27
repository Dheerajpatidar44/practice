"""
=============================================================================
Phase 3: Lists, Dictionaries & Nested Models
Topic: Lists of Nested Models & Complex JSON Structures
=============================================================================
Complex real-world APIs aksar lists of objects return karti hain,
jaise ek E-commerce Order ke andar multiple Order Items hote hain:
Order -> items: list[OrderItem]
"""

from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    product_id: int
    product_name: str
    quantity: int = Field(gt=0, description="Quantity 1 ya usse zyada honi chahiye")
    price_per_unit: float = Field(gt=0)

    @property
    def total_item_price(self) -> float:
        return self.quantity * self.price_per_unit

class Order(BaseModel):
    order_id: str
    customer_name: str
    items: list[OrderItem] = Field(min_length=1, description="Order me kam se kam 1 item hona chahiye")

    @property
    def grand_total(self) -> float:
        return sum(item.total_item_price for item in self.items)

print("=" * 60)
print("1. Parsing Complex Structured JSON into List of Models")
print("=" * 60)

raw_order_json = {
    "order_id": "ORD-2026-9981",
    "customer_name": "Dheeraj Patidar",
    "items": [
        {"product_id": 101, "product_name": "Mechanical Keyboard", "quantity": 1, "price_per_unit": 2499.0},
        {"product_id": 102, "product_name": "Gaming Mouse", "quantity": 2, "price_per_unit": 799.0},
        {"product_id": 103, "product_name": "Mousepad", "quantity": 1, "price_per_unit": 299.0}
    ]
}

# Entire nested structure automatically parsed!
order = Order(**raw_order_json)

print(f"Order ID      : {order.order_id}")
print(f"Customer      : {order.customer_name}")
print(f"Total Items   : {len(order.items)}")
print("-" * 40)
for idx, item in enumerate(order.items, start=1):
    print(f"  {idx}. {item.product_name} x {item.quantity} = Rs. {item.total_item_price}")
print("-" * 40)
print(f"Grand Total   : Rs. {order.grand_total}")
