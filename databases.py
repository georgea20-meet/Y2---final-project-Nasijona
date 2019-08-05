from model import Base, Product

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, maker, picture):
  product_object = Product(
    name=name,
    price=price,
    maker=maker,
    picture=picture)
  session.add(user_object)
  session.commit()
