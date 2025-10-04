#citeos - AI tools that can extract data from image

# Import libraries
from fastapi import FastAPI, Depends
from model import *
from config import session, engine
import database_model
from sqlalchemy.orm import Session

# Create an object/instance of FASTAPI
app = FastAPI()

# Create all tables in the database (if they don't exist) using the metadata from Base
# Work of Base is Inheritance
database_model.Base.metadata.create_all(bind=engine)

# Define a GET endpoint at root URL '/'
@app.get("/") # @app.get -- Decorator or End point (i.e. /)
def greet(): # Function to handle request
    return "Hello Prathamesh Jadhav"  # Return a simple string response

### Create a list of sample products using Pydantic models
products = [
    Product(id=1,name="phone",description="Budget Phone",price=25620,quantity=10),
    Product(id=2, name="laptop", description="Coding Laptop", price=78105, quantity=6),
    Product(id=3, name="Table", description="Table", price=265, quantity= 60),
    Product(id=4, name="laptop", description="Pen", price=150.25, quantity=70)
]

# Dependancy function to provide a DB session for endpoints
def get_db():
    db = session() # create a new session instance
    try:
        yield db # provide the session to the endpoint
    finally:
        db.close() # Close session after request is done

# Function to initialize database with sample products
# function to add the data into mysql server
def init_db():
    db = session() # Open a new session
    count = db.query(database_model.Products).count() # Check how many product exist

    if count==0: # if table is empty
        for product in products:
        ## ** -- unpacking pydantic model dictionary into SQLAlchemy model
            db.add(database_model.Products(**product.model_dump()))
        db.commit() # save changes to the database
init_db() # Call function to initialize DB

# Endpoint to get all products
@app.get("/products")
# db: Session = Depends(get_db) -- > inject the DB session
def get_products(db: Session = Depends(get_db)):
    db_products = db.query(database_model.Products).all() # Query all products from DB
    return db_products # Currently returning static list instead of DB query

# Endpoint to get a product by ID
# Using parameter to read the only one product
@app.get("/products/{id}")
def get_product_by_id(id:int,db: Session = Depends((get_db)) ):
    db_product = db.query(database_model.Products).filter(database_model.Product.id == id).first() # Loop through static list
    if db_product:
        return db_product # return the product if found
    return "product not found {by ID}" # return message if not found

# Create a function that can add the product / Endpoint to add a new product
# Implementation of post function
@app.post("/products")
def add_product(product:Product, db: Session = Depends((get_db))): #
    # append or add to static list (not DB)
    db.add(database_model.Products(**product.model_dump()))
    db.commit()
    return "Added to DB" # return added product


# Update the product
# Endpoint to update an existing product
@app.put("/products")
def update_product(id:int, product:Product,db: Session = Depends((get_db))):
    db_product = db.query(database_model.Products).filter(database_model.Product.id == id).first()  # Loop through static list
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "updated Successufully"
    else:
        return "No product found {update}" # return message if product ID not found

# Delete the product in Product
# Endpoint to delete a product
@app.delete("/products")
def delete_product(id:int, db: Session = Depends((get_db))):
    db_product = db.query(database_model.Products).filter(database_model.Product.id == id).first()  # Loop through static list
    if db_product:
        db_product.delete(db_product)
        db.commit()
        return "Product deleted" # return success meessage
    else:
        return "No product found {delete}" # return message if ID not found
