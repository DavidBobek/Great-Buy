from concurrent.futures import process
from time import process_time

from numpy import append
from product import Product
from product import Basket
from user import User
import re


def registration():
    name = input("Enter your name: ")
    email_address = input("Enter your email address: ")
    password = input("Enter your password: ")
    age = input("Enter your age: ")

    validation(name, email_address, password, age)


def validation(name, email_address, password, age):
    if not name.isalpha():
        # need some message that the process is starting once again
        registration()

    email_regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )

    if not re.fullmatch(email_regex, email_address):
        registration()

    if not re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
        registration()

    for x in age:
        if not re.fullmatch(r"[0-9]", x):
            registration()


#registration()


def filterby_proccesor(warehouse, users_choice):

    processorAMD_5 = []
    processorAMD_7 = []
    processorAMD_9 = []

    processorIntel_3 = []
    processorIntel_5 = []
    processorIntel_7 = []
    processorIntel_9 = []

    for x in warehouse:
        if x.processor == "AMD Ryzen 5":
            processorAMD_5.append(x)

        if x.processor == "AMD Ryzen 7":
            processorAMD_7.append(x)

        if x.processor == "AMD Ryzen 9":
            processorAMD_9.append(x)
            print(len(processorAMD_9))

        if x.processor == "Intel Core i3":
            processorIntel_3.append(x)

        if x.processor == "Intel Core i5":
            processorIntel_5.append(x)

        if x.processor == "Intel Core i7":
            processorIntel_7.append(x)

        if x.processor == "Intel Core i9":
            processorIntel_9.append(x)

    if users_choice == "AMD Ryzen 5":
        print(f"Returned all processors {processorAMD_5}")
        return processorAMD_5

    if users_choice == "AMD Ryzen 7":
        print(f"Returned all processors {processorAMD_7}")
        return processorAMD_7

    if users_choice == "AMD Ryzen 9":
        print(f"Returned all processors {processorAMD_9}")
        return processorAMD_9

    if users_choice == "Intel Core i3":
        print(f"Returned all processors {processorIntel_3}")
        return processorIntel_3

    if users_choice == "Intel Core i5":
        print(f"Returned all processors {processorIntel_5}")
        return processorIntel_5

    if users_choice == "Intel Core i7":
        print(f"Returned all processors {processorIntel_7}")
        return processorIntel_7

    if users_choice == "Intel Core i9":
        print(f"Returned all processors {processorIntel_9}")
        return processorIntel_9


def filterby_storagetype(warehouse, users_choice):
    SSD_type = []
    HDD_type = []

    for x in warehouse:
        if x.storage_type == "SSD":
            SSD_type.append(x)

    for x in warehouse:
        if x.storage_type == "HDD":
            HDD_type.append(x)

    if users_choice == "HDD":
        return HDD_type

    if users_choice == "SSD":
        return SSD_type

    # search





    """. Filter = Is going to then display Laptops that can be filtered by = processor (Intel Core
i9,Intel Core i7, Intel Core i5,Intel Core i3,AMD Ryzen 9,AMD Ryzen 7,AMD Ryzen
5),Storage type(SSD\HDD), Color(Black,Silver,White,Gray),Screen Size"""


warhouseitems = []

userchoice = "AMD Ryzen 9"


def mainfilter(option):
    if option == "processor":
        return filterby_proccesor(warhouseitems, userchoice)

    if option == "storage":
        return filterby_storagetype(warhouseitems, userchoice)


davidko = User("david", "dbobek", "5454", 69)
basket1 = Basket()
basket1.calculate_total_value()

davidko.assignbasket(basket1)

print(basket1.items)
# desc
produkt1 = Product(
    "Produkt 1", "brand", 2, "screensize", "time", "AMD Ryzen 9", "b", "a", "helloo"
)
produkt2 = Product(
    "Produkt 2", "brand", 2, "screensize", "time", "AMD Ryzen 9", "b", "a", "helloo"
)
produkt3 = Product(
    "Produkt 3", "brand", 4, "screensize", "time", "Intel Core i5", "b", "a", "helloo"
)
produkt4 = Product(
    "Produkt 4", "brand ", 8, "screensize", "time", "Intel Core i3", "b", "a", "helloo"
)

warhouseitems.append(produkt1)
warhouseitems.append(produkt2)
warhouseitems.append(produkt3)
warhouseitems.append(produkt4)


basket1.additem(produkt1)
basket1.additem(produkt2)
basket1.additem(produkt3)
basket1.additem(produkt4)

basket1.calculate_total_value()
basket1.removeitem(produkt2)
print(basket1.check_items())
basket1.calculate_total_value()

print(basket1.check_items())


# objects
print(mainfilter("processor"))

# set to filter for AMD Ryzen 9
for x in mainfilter("processor"):
    print(x.processor)





from Visual import *

import sys


class firstApp(Ui_MainWindow):
    def __init__(self,window):
        
        self.setupUi(window)
        #this line connect the button called filter_button with a local function ShowMe
        self.filter_button.clicked.connect(self.getUsers_processor)
        
        #OPted for my own group boxes
        
        self.radio_procesors = []
        self.radio_procesors.append(self.Intel_9)
        self.radio_procesors.append(self.Intel_7)
        self.radio_procesors.append(self.Intel_5)
        self.radio_procesors.append(self.Intel_3)
        
        self.radio_procesors.append(self.AMD9)
        self.radio_procesors.append(self.AMD7)
        self.radio_procesors.append(self.AMD5)
        
        
        

    
    def getUsers_processor(self):
        #need to cycle through all of the groupboxes
        
        for x in self.radio_procesors:
            if x.isChecked():
                print("dsfg")
                #works, stores a text of the processor
                pickedprocessor = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                filterby_proccesor(warhouseitems, pickedprocessor)
                print(f"Filtering {pickedprocessor}")
            
      
    



#ALLOWS US TO ACTUALLY SEE THE MENU
#very important

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

#instance of the class

ui = firstApp(MainWindow)


from registration import *


class registration_window(Registration_Ui):
    def __init__(self,window):
        self.setupUi(window)
        #this line connect the button called filter_button with a local function ShowMe
        self.proceed_button.clicked.connect(self.collect_data)
        
        
        
        
    def collect_data(self):
        
        #figure out how to get the text
        entry_name = self.name_entry.text
        entry_email = self.email_entry.text 
        entry_password = self.password_entry.text
        print(entry_email)
        
            
        #wooorks
        ui = firstApp(MainWindow)
        MainWindow.show()


reg = registration_window(MainWindow)
MainWindow.show()
app.exec()
