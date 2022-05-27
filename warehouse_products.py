from product import Product
import random  
import time


processors= ["AMD Ryzen 9","AMD Ryzen 7","AMD Ryzen 5","Intel Core i9","Intel Core i7","Intel Core i5","Intel Core i3"]
colors = ["Silver","Black","White","Gray"]
storages = ["SSD","HDD"]
brands = ["ASUS","LENOVO","ACER","HP"]

prods = []

for x in range(10000):
    name = f"Product {x}"
    brand = random.choice(brands)
    processor = random.choice(processors)
    color = random.choice(colors)
    storage = random.choice(storages)
    price = random.randrange(700,1200)
    screen = random.randrange(9,20)
    curr_time = time.localtime()
    description = f"This is a great product!"
    
    product = Product(name,brand,price,str(screen),curr_time,processor,storage,color,description)
    
    prods.append(product)
    
    
    

global allitems
allitems = []

allitems = allitems+prods
