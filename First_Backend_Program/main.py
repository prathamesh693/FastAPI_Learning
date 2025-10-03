# Import Fast API library
from fastapi import FastAPI
from models import Product

# Create an object of FASTAPI
app = FastAPI()

@app.get("/") # @app.get -- Decorator or End point (i.e. /)
def greet():
    return "Hello Prathamesh Jadhav"

### create a list of product
products = [
    Product(id=1,name="phone",description="Budget Phone",price=99,quantity=10),
    Product(id=2, name="laptop", description="Coding Laptop", price=991, quantity=6)
]

@app.get("/products")
def get_products():
    return products

# Using parameter to read the only one product
@app.get("/products/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

# Create a function that can add the product
# Implementation of post function
@app.post("/products")
def add_product(product:Product): #
    # append or add the product into products list
    products.append(product)
    return product

# Update the product
@app.put("/products")
def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i]. id ==id:
            products[i] = product
            return "Product added"

    return "No product found"

# Delete the product in Product
@app.delete("/products")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Product deleted"
    return "No product found"
