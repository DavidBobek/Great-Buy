

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
    def __init__(
       # *,
        self,
        name,
        brand,
        price,
        screensize,
        time_of_purchase,
        processor,
        storage_type,
        color,
        description,
    ):
        self.name = name
        self.price = price
        self.id = str(uuid.uuid4())
        self.brand = brand
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

    def additem(self, item):
        self.items.append(item)

    def removeitem(self, item):
        self.items.remove(item)



    def calculate_total_value(self):
        totalValue = 0
        for x in self.items:
            totalValue += x.price

       
        return totalValue

    def check_items(self):
        itemnames = []
        for x in self.items:
            itemnames.append(x.name)

        return itemnames


