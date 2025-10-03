# Import libraries
from fastapi import FastAPI
from models import Product

# Create an object/instance of FastAPI, which will be our main app
app = FastAPI()

# Define a GET endpoint for the root URL "/"
@app.get("/")  # Decorator to define HTTP GET method for "/"
def greet():  # Function that will run when someone accesses "/"
    return "Hello Prathamesh Jadhav"  # Return a greeting message

# Create a list of products with sample data
products = [
    Product(id=1, name="phone", description="Budget Phone", price=99, quantity=10),  # First product
    Product(id=2, name="laptop", description="Coding Laptop", price=991, quantity=6)  # Second product
]

# Define a GET endpoint to fetch all products
@app.get("/products")  # Endpoint URL "/products"
def get_products():  # Function executed when "/products" is accessed
    return products  # Return the full list of products

# Define a GET endpoint to fetch a product by its ID
@app.get("/products/{id}")  # Endpoint with a path parameter "id"
def get_product_by_id(id: int):  # Function accepts an integer "id"
    # Loop through all products to find the one with matching ID
    for product in products:
        if product.id == id:  # Check if product ID matches
            return product  # Return the matching product
    # If no product found, return this message
    return "product not found"

# Define a POST endpoint to add a new product
@app.post("/products")  # HTTP POST method for adding new data
def add_product(product: Product):  # Accept a product object in request body
    products.append(product)  # Append the new product to the list
    return product  # Return the added product as confirmation

# Define a PUT endpoint to update an existing product
@app.put("/products")  # HTTP PUT method for updating data
def update_product(id: int, product: Product):  # Accept ID and updated product data
    # Loop through the products to find the one with matching ID
    for i in range(len(products)):
        if products[i].id == id:  # Check for matching ID
            products[i] = product  # Replace the old product with the updated one
            return "Product added"  # Return success message
    # If no product with the given ID is found
    return "No product found"

# Define a DELETE endpoint to remove a product
@app.delete("/products")  # HTTP DELETE method for deleting data
def delete_product(id: int):  # Accept ID of product to delete
    # Loop through the products to find the one with matching ID
    for i in range(len(products)):
        if products[i].id == id:  # Check for matching ID
            del products[i]  # Delete the product from the list
            return "Product deleted"  # Return success message
    # If no product with the given ID is found
    return "No product found"
