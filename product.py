from cgi import print_exception


""" 
price
brand
screensize
id
time of buy
name
processor
storage type
color
description

"""
import uuid
import datetime

class Product:
    def __init__(self,name,brand,price,screensize,time_of_purchase,processor,storage_type,color,description):
        self.name = name
        self.price = price
        self.id = str(uuid.uuid4())
        self.brand = brand
        self.price = price
        self.screensize = screensize
        self.time_of_purchase = time_of_purchase
        self.processor = processor
        self.storage_type = storage_type
        self.color = color
        self.description = description
        
        
class Basket:
    def __init__(self):
        self.items = []
        self.user = None
        
    #works
    def additem(self,item):
        self.items.append(item)
        
    def removeitem(self,item):
        self.items.remove(item)
        
        
    #works
    def calculate_total_value(self):
        totalValue = 0
        for x in self.items:
            totalValue += x.price
        
        print(totalValue)
        return totalValue
    
    def check_items(self):
        itemnames = []
        
        #appending some random bullshit
        for x in self.items:
            itemnames.append(x.name)
    
        return itemnames
    
""" produkt1 = Product("Produkt 1","b",2,"a","b","a","b","a","helloo")
produkt2 = Product("Produkt 2","b",2,"a","b","a","b","a","helloo")
produkt3 = Product("Produkt 3","b",4,"a","b","a","b","a","helloo")
produkt4 = Product("Produkt 4","b",8,"a","b","a","b","a","helloo")

basket1 = Basket()

basket1.additem(produkt1)
basket1.additem(produkt2)
basket1.additem(produkt3)
basket1.additem(produkt4)

basket1.calculate_total_value() """