
import uuid


class User:
    def __init__(self, name, email, password, id =str(uuid.uuid4()) ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.basket = None
        self.sellings = {}
  
    def assignbasket(self, basket):
        self.basket = basket

    def addreview(self, review, product):
        product.reviews.append(review)

