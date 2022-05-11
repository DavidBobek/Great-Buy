from audioop import reverse
from cgitb import small
from concurrent.futures import process
from heapq import merge
from time import process_time
from typing import final
from unittest import result

from numpy import append
from View_Item import View_Item_UI
from product import Product
from product import Basket
from user import User
import re



def validation(name, email_address, password):
    correctness = 1
    if not name.isalpha():
        # need some message that the process is starting once again
        correctness = 0
    email_regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )

    if not re.fullmatch(email_regex, email_address):
        correctness = 0

    if not re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
        correctness = 0

    if correctness ==1:
        return "Valid"
    else:
        return "Not Valid"
    


#registration()


def filterby_proccesor(warehouse, users_choice):

    """ processorAMD_5 = []
    processorAMD_7 = []
    processorAMD_9 = []

    processorIntel_3 = []
    processorIntel_5 = []
    processorIntel_7 = []
    processorIntel_9 = []
     """
    
    final = []
    #this actually might be the final solution
    for x in warehouse:
        
        if users_choice == {}:
            return final
        if x.processor == users_choice["processor"]:
            final.append(x)
            
        else:
            pass
  
    if len(final) == 0:
        return final
    else:
        return final

def filterby_screensize(warehouse,users_choice): 


    smallest = []
    lowmid = []
    mid = []
    high_mid = []
    high = []
    
    
    final = []
    for x in warehouse:
        
        if float(x.screensize) < 11:
            smallest.append(x)       
             
        if float(x.screensize) >= 11 and float(x.screensize) < 14:
            lowmid.append(x)
            
        if float(x.screensize) >= 14 and float(x.screensize) < 15.6:
            mid.append(x)
            
        if float(x.screensize) >= 15.6  and float(x.screensize) < 17.3:
            high_mid.append(x)    
             
        if float(x.screensize) > 17.3:       
            high.append(x)

    
    if users_choice == {'screensize': "x<11"}:
        
        return smallest
    if users_choice == {'screensize': '11\'\'≥x<14"'}:
        
        return lowmid
    if users_choice =={'screensize':  '14"≥x<15.6"'}:
    
        return mid
    if users_choice =={'screensize':  '15.6\'\'≥x<17.3"'}:
      
        return high_mid
    if users_choice == {'screensize': 'x≥17.3"'}:
    
        return high

   
            
    #this actually might be the final solution
    for x in warehouse:
        
        if users_choice == {}:
            return final
        if x.screensize == users_choice["screensize"]:
            final.append(x)
        else:
            pass
  
    if len(final) == 0:
        return final
    else:
        return final

def filterby_color(warehouse,users_choice): 
    
    final = []

    for x in warehouse:
        if users_choice == {}:
            return final
        if x.color == users_choice["color"]:
            final.append(x)

    if len(final) == 0:
        return final
    else:
        return final



def filterby_storagetype(warehouse, users_choice):
    final = []
    #this actually might be the final solution
    for x in warehouse:
        
        if users_choice == {}:
            return final
        if x.storage_type == users_choice["storage_type"]:
            final.append(x)
        else:
            pass
 
    if len(final) == 0:
        return final
    else:
        return final



from Visual import *
from items import Scrolling
import sys

import database

class firstApp(Ui_MainWindow):
    
    def __init__(self,window):
        
        self.setupUi(window)
        #this line connect the button called filter_button with a local function ShowMe
        self.filter_button.clicked.connect(self.getUsers_processor)
        self.filter_button.clicked.connect(self.getUsers_sizes)
        self.filter_button.clicked.connect(self.getUsers_color)
        self.filter_button.clicked.connect(self.getUsers_type_of_storage)
        self.filter_button.clicked.connect(self.mainfilter)
    
        
        
        self.login_button.clicked.connect(self.openregistration)
        
        
    
    
    
    
        #OPted for my own group boxes
        #Processors
        self.radio_procesors = []
        self.radio_procesors.append(self.Intel_9)
        self.radio_procesors.append(self.Intel_7)
        self.radio_procesors.append(self.Intel_5)
        self.radio_procesors.append(self.Intel_3)
        
        self.radio_procesors.append(self.AMD9)
        self.radio_procesors.append(self.AMD7)
        self.radio_procesors.append(self.AMD5)
        
        
        #Screensizes
        self.radio_screensizes = []
        self.radio_screensizes.append(self.smallest)
        self.radio_screensizes.append(self.lowermid)
        self.radio_screensizes.append(self.mid)
        self.radio_screensizes.append(self.uppermid)
        self.radio_screensizes.append(self.largest)
        
        self.radio_color = []
        self.radio_color.append(self.c_black)
        self.radio_color.append(self.c_silver)
        self.radio_color.append(self.c_white)
        self.radio_color.append(self.c_gray)
        
        self.radio_storage = []
        self.radio_storage.append(self.storage_ssd)
        self.radio_storage.append(self.storage_HDD)
        
        self.warhouseitems = []



    
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
            "Produkt 3", "MAC", 4, "16", "time", "Intel Core i5", "HDD", "White", "helloo"
        )
        produkt14 = Product(
            "Produkt 4", "ACER ", 8, "14.5", "time", "Intel Core i5", "HDD", "Silver", "helloo"
        )
        produkt15 = Product(
            "Produkt 5", "ASUS", 2, "14.8", "time", "AMD Ryzen 7", "HDD", "Gray", "helloo"
        )

        self.warhouseitems.append(produkt1)
        self.warhouseitems.append(produkt2)
        self.warhouseitems.append(produkt3)
        self.warhouseitems.append(produkt4)
        self.warhouseitems.append(produkt5)
        self.warhouseitems.append(produkt6)
        self.warhouseitems.append(produkt7)
        self.warhouseitems.append(produkt8)
        self.warhouseitems.append(produkt9)
        self.warhouseitems.append(produkt10)
        self.warhouseitems.append(produkt11)
        self.warhouseitems.append(produkt12)
        self.warhouseitems.append(produkt13)
        self.warhouseitems.append(produkt14)
        self.warhouseitems.append(produkt15)
                
    def openregistration(self):
     
        self.window = QtWidgets.QMainWindow()
        self.ui = Registration_Ui()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.proceed_button.clicked.connect(self.checking)
        
        
        
    def checking(self):
        entry_name = self.ui.name_entry.text()
        entry_email = self.ui.email_entry.text()
        entry_password = self.ui.password_entry.text()
        
        
        if validation(entry_name,entry_email,entry_password) == "Valid":
            if database.controlling(entry_email) == "Not":    
                newUser = User(entry_name,entry_email,entry_password,18)
                database.registering(newUser)
                print("User registered")
                self.window.hide()
                
            else:
                self.ui.name_entry.setText("User with this email adress already exists")
                self.ui.email_entry.setText("User with this email adress already exists")
                self.ui.password_entry.setText("User with this email adress already exists")
                
                #check if user exists, if not than write to database
            
            #how to check if there is something in the database
            
            
            
            
        else:
            self.ui.name_entry.setText("")
            self.ui.email_entry.setText("")
            self.ui.password_entry.setText("")
    
    
        
    
    
    def getUsers_processor(self):
        # THIS FUNCTION NEEDS TO CHECK ALL PARAMS!!!!!
        
        
        
        #need to cycle through all of the groupboxes
        
        for x in self.radio_procesors:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedprocessor = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                #filterby_proccesor(self.warhouseitems, pickedprocessor)
                print(f"Filtering {pickedprocessor}")
                final_result = {"processor":pickedprocessor}
                return final_result
        return {}
               
                
    def getUsers_sizes(self):
        # THIS FUNCTION NEEDS TO CHECK ALL PARAMS!!!!!
        
        
        
        #need to cycle through all of the groupboxes
        
        for x in self.radio_screensizes:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedscreensize = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                #filterby_screensize(self.warhouseitems, pickedscreensize)
                print(f"Filtering {pickedscreensize}")
                
                final_result = {"screensize":pickedscreensize}
                return final_result
        return {}
    def getUsers_color(self):
        # THIS FUNCTION NEEDS TO CHECK ALL PARAMS!!!!!
        
        
        
        #need to cycle through all of the groupboxes
        
        for x in self.radio_color:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedscolor = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                #filterby_color(self.warhouseitems, pickedscolor)
                print(f"Filtering {pickedscolor}")
                final_result = {"color":pickedscolor}
                return final_result
        return {}
      
    def getUsers_type_of_storage(self):
        for x in self.radio_storage:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedstorage = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                #filterby_storagetype(self.warhouseitems, pickedstorage)
                print(f"Filtering {pickedstorage}")
                final_result = {"storage_type":pickedstorage}
                return final_result
        return {}
        
        
        
        
    #popping up a new window          
    def View_more(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = View_Item_UI()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
        
        #print("shit")
    #i have isolated the button from the original list Everything new 
    def hookupmainbuttons(self,Everythingnew):
        buttons = []
        for x in Everythingnew:
            buttons.append(x[1])
            
            
        #assigned every single button to a function View_more
        #not using self because it doesnt actually belong to this class
        for x in buttons:
            x.clicked.connect(self.View_more)
            
            
    def hook_item_functions(self,buttons):
        for x in buttons.button_list:
            x.clicked.connect(self.View_more)
    
    """    def openProducts(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Scrolling(20)
        self.ui.setupUi(self.window)
        self.window.show() """
        
    
    def mainfilter(self):
        #gathering the color from the inputs
        fav_color = self.getUsers_color()
        fav_processor = self.getUsers_processor()
        fav_size = self.getUsers_sizes()
        fav_storage = self.getUsers_type_of_storage()
        
       
        #creating multiple variables that are going to hold filtered items just by a single category
        storage_pick = filterby_storagetype(self.warhouseitems,fav_storage)
        color_pick = filterby_color(self.warhouseitems,fav_color)
        screensize_pick = filterby_screensize(self.warhouseitems,fav_size)
        processor_pick = filterby_proccesor(self.warhouseitems,fav_processor)
        
        
        #all filtered categories
        all = storage_pick+color_pick+screensize_pick+processor_pick

        
        #checking which parameters are being filtered
        Not_null_params = []
        
        if len(storage_pick) > 0:
            Not_null_params.append("storage_type")
            
        
        if len(color_pick) > 0:
            Not_null_params.append("color")
            
        
        if len(processor_pick) > 0:
            Not_null_params.append("processor")
            
        
        if len(screensize_pick) > 0:
            Not_null_params.append("screensize")
            

        print(Not_null_params)

        
        filtered_elements = []
        final_products = []
        all = set(all)
        for x in all:

            
            
            if "color" in Not_null_params:
                if x.color == fav_color.get("color"):
                    filtered_elements.append(x)
                    
            
            if "processor" in Not_null_params:
                if x.processor == fav_processor.get("processor"):
                    filtered_elements.append(x)
                    
            
            if "storage_type" in Not_null_params:
                if x.storage_type == fav_storage.get("storage_type"):
                    filtered_elements.append(x)
                    
            my_Category = {}
            if "screensize" in Not_null_params:
                
                
                if float(x.screensize) <11:
                    my_Category =  "x<11"
                
                if float(x.screensize)>=11 and float(x.screensize)<14:
                    my_Category =  '11\'\'≥x<14"'
                    
                if float(x.screensize)>=14 and float(x.screensize)<15.6:
                    
                    my_Category =  '14"≥x<15.6"'
                    
                if float(x.screensize)>=15.5 and float(x.screensize) <17.3:
                    my_Category =  '15.6\'\'≥x<17.3"'
                if float(x.screensize) >17.3:
                    my_Category = 'x≥17.3"'
                    
                    
                if my_Category == fav_size.get("screensize"):
                    filtered_elements.append(x)
                    
            
            if (fav_color == {} or fav_color.get("color") == x.color) and  (fav_processor == {} or fav_processor.get("processor") == x.processor) and (fav_storage == {} or fav_storage.get("storage_type") == x.storage_type)  and (my_Category == {} or my_Category==fav_size.get("screensize")):
                final_products.append(x)
        print(final_products)
        print("\n")
        print("fuck we are done")
        #self.openProducts()
        #https://www.youtube.com/watch?v=TXZkHy2koyo
        #prods = Scrolling(len(final_products))
        
       
     
        
        for x in range(1,len(final_products)):
            ui.make_groupbox("C,","c",x)
            
     
        
        
        self.View_items(final_products)
        return final_products

    def View_items(self,_items):
        self.window = QtWidgets.QMainWindow()
        self.scroll = Scrolling(_items)
        ui.hook_item_functions(self.scroll)
       
       
        

#ALLOWS US TO ACTUALLY SEE THE MENU
#very important



#instance of the class

from registration import *




from PyQt5.QtWidgets import QMessageBox,QApplication,QWidget,QScrollArea,QFormLayout,QLabel,QPushButton,QGroupBox,QVBoxLayout
from PyQt5 import QtGui
import sys



start = 0
while start == 0:
    start = 2
        
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #instance of the class

    ui = firstApp(MainWindow)
    Everythingnew = []
    
    #FUNCTION THAT IS CALLING STUFF FROM VISUAL TO MAKE IT MORE CLEANER
    #1 to 5 means actually 1 to 4, limitation of for loop
    for x in range(1,3):  
        #Item = name
        #
        #x = iterator  
        
        #NEED TO THINK OF A WAY ON HOW TO ACTUALLY CONNECT FILTERED ELEMENTS TO THE GROUP BOXES
        IterationItems = ui.make_groupbox("Item","dopice",x)
        Everythingnew.append(IterationItems)
        
        
        
        
   
    #calling the function to assign the buttons
    ui.hookupmainbuttons(Everythingnew)

    MainWindow.show()

    app.exec()
   
