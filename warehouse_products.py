from turtle import screensize
from product import Product
produkt1 = Product(
    "Produkt 1", "ASUS", 2, "12", "time", "Intel Core i7", "SSD", "Black", "helloo"
)
produkt2 = Product(
    "Produkt 2", "LENOVO", 2, "15.6", "time", "AMD Ryzen 9", "SSD", "Gray", "helloo"
)
produkt3 = Product(
    "Produkt 3", "MAC", 4, "20", "time", "Intel Core i5", "HDD", "Gray", "helloo"
)
produkt4 = Product(
    "Produkt 4", "ACER ", 8, "11", "time", "Intel Core i3", "SSD", "Silver", "helloo"
)
produkt5 = Product(
    "Produkt 5", "ASUS", 2, "12", "time", "AMD Ryzen 9", "SSD", "White", "helloo"
)
produkt6 = Product(
    "Produkt 1", "ASUS", 2, "15", "time", "Intel Core i3", "SSD", "Black", "helloo"
)
produkt7 = Product(
    "Produkt 2", "LENOVO", 2, "15.6", "time", "AMD Ryzen 9", "SSD", "Black", "helloo"
)
produkt8 = Product(
    "Produkt 3", "MAC", 4, "20", "time", "Intel Core i9", "HDD", "White", "helloo"
)
produkt9 = Product(
    "Produkt 4", "ACER ", 8, "17", "time", "Intel Core i3", "HDD", "Silver", "helloo"
)
produkt10 = Product(
    "Produkt 5", "ASUS", 2, "10", "time", "AMD Ryzen 5", "SSD", "Gray", "helloo"
)
produkt11 = Product(
    "Produkt 1", "ASUS", 2, "14", "time", "AMD Ryzen 5", "SSD", "Gray", "helloo"
)
produkt12 = Product(
    "Produkt 2", "LENOVO", 2, "13.6", "time", "AMD Ryzen 7", "SSD", "Black", "helloo"
)
produkt13 = Product(
    "Produkt 3", "MAC", 4, "16", "time", "Intel Core i5", "SSD", "White", "helloo"
)
produkt14 = Product(
    "Produkt 4", "ACER ", 8, "14.5", "time", "Intel Core i5", "HDD", "Silver", "helloo"
)
produkt15 = Product(
    "Produkt 5", "ASUS", 2, "14.8", "time", "AMD Ryzen 7", "HDD", "Gray", "helloo"
)
produkt16 = Product(
    "Produkt 5", "ASUS", 2, "15.8", "time", "AMD Ryzen 5", "HDD", "White", "helloo"
)
produkt17 = Product(
    "Produkt 5", "ASUS", 2, "11.8", "time", "AMD Ryzen 5", "HDD", "Black", "helloo"
)
produkt18 = Product(
    "Produkt 5", "ASUS", 2, "11.8", "time", "AMD Ryzen 9", "SSD", "White", "helloo"
)
produkt19 = Product(
    "Produkt 5", "ASUS", 2, "13.8", "time", "AMD Ryzen 7", "SSD", "White", "helloo"
)

produkt20 = Product(
    "Produkt 5", "ASUS", 2, "16.8", "time", "AMD Ryzen 7", "SSD", "Gray", "helloo"
)
produkt21 = Product( 
    "Produkt 5", "ASUS", 2, "18.8", "time", "AMD Ryzen 7", "SSD", "Gray", "helloo"
)
""" import random

newlist = []


radio_procesors = [Intel_9,Intel_7,Intel_5,Intel_3,AMD5,AMD7,AMD9]
        
radio_screensizes = [smallest,lowermid,mid,uppermid,largest]        
radio_color = [c_black,c_silver,c_white,c_gray]  
        
radio_storage = [
storage_ssd,
storage_HDD]
for x in range(1,100): """
  
import random  
import time

"Produkt 4", "ACER ", 8, "14.5", "time", "Intel Core i5", "HDD", "Silver", "helloo"
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
    screen = random.randrange(10,20)
    curr_time = time.localtime()
    description = f"This is a great product!"
    
    product = Product(name,brand,price,str(screen),curr_time,processor,storage,color,description)
    
    prods.append(product)
    
    
    

global allitems
allitems = []

allitems = allitems+prods
