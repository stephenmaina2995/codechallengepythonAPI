# import sqlite3

# # Connect to the database or create it if it doesn't exist
# conn = sqlite3.connect('student.db')

# # Create a cursor object to interact with the database
# cursor = conn.cursor()

# # Create a table to store the data
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     first_name TEXT,
#                     last_name TEXT,
#                     email TEXT,
#                     gender TEXT
#                 )''')

# # Insert the data into the table
# cursor.execute('''INSERT INTO users (id, first_name, last_name, email, gender)
#                   VALUES (1, 'Clem', 'Cowap', 'ccowap0@cloudflare.com', 'Male')''')

# # Commit the changes and close the connection
# conn.commit()
# conn.close()
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customer'
    first_name = Column (String, nullable=False)
    last_name = Column (String, nullable=False)
    email = Column (String, nullable=False)
    gender = Column (String, nullable=False)

    engine = create_engine("sqlite:///db.db")
    Base.metadata.create_all(engine)
    sessionmaker = sessionmaker(bind=engine)