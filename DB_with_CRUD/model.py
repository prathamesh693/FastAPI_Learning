# Import pydantic BaseModel for data validation
from pydantic import BaseModel

# Define product schema for API requests/responses
class Product(BaseModel):
    id: int # Product ID
    name: str # product name
    description: str # product description
    price: float # product price
    quantity: int # product quantity