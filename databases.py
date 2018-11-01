from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
MAX_PRICE = 300
# Write your functions to interact with the database here :

def create_product(name, price, color, description):
	
	new_product = Product(product_name = name, price = price, color = color, description = description)
	session.add(new_product)
	session.commit()
def update_product(name, price, color):
  #TODO: complete the functions (you will need to change the function's inputs)
    if price > MAX_PRICE:
  	    print("the price is too high!")
    else:
	    product = session.query(Product).filter_by(product_name = name).first()
	    product.price = price
	    product.color = color

def delete_product(id):
 	session.query(Product).filter_by(id = id).delete()
 	session.commit()


def get_product(id):
	product = session.query(Product).filter_by(id = id).first()
	return product
# create_product("name", 2, "Red", "this is cool!")


