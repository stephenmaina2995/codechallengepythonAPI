from sqlalchemy import String, Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///db.db")
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# from sqlalchemy import String, Column, Integer
# from sqlalchemy.orm import declarative_base, sessionmaker

# Base = declarative_base()
# class Customer(Base):
#     __tablename__ = 'customer'
#     first_name = Column (String, nullable=False)
#     last_name = Column (String, nullable=False)
#     email = Column (String, nullable=False)
#     gender = Column (String, nullable=False)

#     engine = create_engine("sqlite:///db.db")
#     Base.metadata.create_all(engine)
#     sessionmaker = sessionmaker(bind=engine)