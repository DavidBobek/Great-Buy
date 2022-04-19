#is going to be created after registration
#called from main

"""
name
email
password
age
basket, 1 to 1 relation, USER CAN HAVE ONLY  BASKET
"""



import uuid

class User:
    def __init__(self,name,email,password,age):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.basket = None
        #basket is going to be an object
        
        
        
    def assignbasket(self,basket):
        self.basket = basket