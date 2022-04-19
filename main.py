from product import Product
from product import Basket
from user import User
import re


def registration():
    name = input("Enter your name: ")
    email_address = input("Enter your email address: ")
    password = input("Enter your password: ")
    age = input("Enter your age: ")
    
    validation(name,email_address,password,age)
    

def validation(name,email_address,password,age):
    if not name.isalpha():
        #need some message that the process is starting once again
        registration()

    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if not re.fullmatch(email_regex, email_address):
        registration()
          
    
    if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        registration()
        
        
    for x in age:
        if not re.fullmatch(r'[0-9]',x):
            registration()
registration()



davidko = User("david","dbobek","5454",69)
basket1 = Basket()
basket1.calculate_total_value()

davidko.assignbasket(basket1)

print(basket1.items)

produkt1 = Product("Produkt 1","b",2,"a","b","a","b","a","helloo")
produkt2 = Product("Produkt 2","b",2,"a","b","a","b","a","helloo")
produkt3 = Product("Produkt 3","b",4,"a","b","a","b","a","helloo")
produkt4 = Product("Produkt 4","b",8,"a","b","a","b","a","helloo")



basket1.additem(produkt1)
basket1.additem(produkt2)
basket1.additem(produkt3)
basket1.additem(produkt4)

basket1.calculate_total_value()
basket1.removeitem(produkt2)
print(basket1.check_items())
basket1.calculate_total_value()
 
print(basket1.check_items())