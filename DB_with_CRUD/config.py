# Import a library for configuration.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection URL (MySQL using pymysql driver)
db_url = "mysql+pymysql://root:root@localhost:3306/fastapi"

# Create engine to manage connections
# Help to connect with database (in which database we are using)
engine = create_engine(db_url)

# Create a session using sessionmaker()
# Create session factory to manage DB Sessions
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
