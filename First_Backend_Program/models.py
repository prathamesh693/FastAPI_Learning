# Import BaseModel from pydantic
# Pydantic is used for data validation and parsing in FastAPI

from pydantic import BaseModel

# define a product model class inheriting from BaseModel
class Product(BaseModel):
    id: int # product ID as an integer
    name: str # product name as a string
    description: str # product description as a string
    price: float # product price as a float
    quantity: int # product quantity as an integer