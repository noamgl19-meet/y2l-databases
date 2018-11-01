from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    # TODO: complete this class
    __tablename__ = "products"
    id = Column(Integer, primary_key = True)
    product_name = Column(String)
    price = Column(Integer)
    color = Column(String)
    description = Column(String)

    def __repr__(self):
    	return "name: " + self.product_name + "\nprice: " + str(self.price) + "\ncolor: " + self.color + "\ndescription: " + self.description