# Import libraries
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Create Base class for ORM models
Base = declarative_base()

# Define product table as a python class
class Products(Base):
    __tablename__ = 'product' # table name in MySQL

    #Define columns in the table
    id = Column(Integer, primary_key=True, index = True) # Primary key column
    name = Column(String(30)) #Product name column
    description = Column(String(100)) # Product description
    price = Column(Float) # Product price
    quantity = Column(Integer) # Product quantity