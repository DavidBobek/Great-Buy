from audioop import reverse
from cgitb import small
from concurrent.futures import process
from time import process_time

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
        if x.processor == users_choice:
            final.append(x)
    #print("done")
    #print(final)
    return final
""" 
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
 """
 
 #FIX IT
def filterby_screensize(warehouse,users_choice): 
    
    #"x<11"
#'11\'\'≥x<14"'
#'14"≥x<15.6"'
#'15.6\'\'≥x<17.3"'
#'x≥17.3"'


#'15.6\'\'≥x<17.3"'
#'x≥17.3"'

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
            high.append

    
    if users_choice == "x<11":
        #print(smallest)
        return smallest
    if users_choice == '11\'\'≥x<14"':
        #print(lowmid)
        return lowmid
    if users_choice == '14"≥x<15.6"':
        #print(mid)
        return mid
    if users_choice == '15.6\'\'≥x<17.3"':
        #print(high_mid)
        return high_mid
    if users_choice == 'x≥17.3"':
        #print(high)
        return high

   
            
    #this actually might be the final solution
    for x in warehouse:
        if x.screensize == users_choice:
            final.append(x)
    #print("done")
    #print(final)
    return final

def filterby_color(warehouse,users_choice): 
    
    final = []
    #this actually might be the final solution
    for x in warehouse:
        if x.color == users_choice:
            final.append(x)
   # print("done")
    #print(final)
    return final



def filterby_storagetype(warehouse, users_choice):
    final = []
    #this actually might be the final solution
    for x in warehouse:
        if x.storage_type == users_choice:
            final.append(x)
    print("done")
    print(final)
    return final
    # search





    """. Filter = Is going to then display Laptops that can be filtered by = processor (Intel Core
i9,Intel Core i7, Intel Core i5,Intel Core i3,AMD Ryzen 9,AMD Ryzen 7,AMD Ryzen
5),Storage type(SSD\HDD), Color(Black,Silver,White,Gray),Screen Size"""








# objects
#print(mainfilter("processor"))

# set to filter for AMD Ryzen 9
""" for x in mainfilter("processor"):
    print(x.processor) """





from Visual import *

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
        
    warhouseitems = []



    
    produkt1 = Product(
        "Produkt 1", "ASUS", 2, "12", "time", "AMD Ryzen 9", "SSD", "Black", "helloo"
    )
    produkt2 = Product(
        "Produkt 2", "LENOVO", 2, "15.6", "time", "AMD Ryzen 9", "SSD", "Black", "helloo"
    )
    produkt3 = Product(
        "Produkt 3", "MAC", 4, "20", "time", "Intel Core i5", "HDD", "White", "helloo"
    )
    produkt4 = Product(
        "Produkt 4", "ACER ", 8, "11", "time", "Intel Core i3", "SSD", "Silver", "helloo"
    )

    warhouseitems.append(produkt1)
    warhouseitems.append(produkt2)
    warhouseitems.append(produkt3)
    warhouseitems.append(produkt4)
            
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
                filterby_proccesor(self.warhouseitems, pickedprocessor)
                print(f"Filtering {pickedprocessor}")
                
                
    def getUsers_sizes(self):
        # THIS FUNCTION NEEDS TO CHECK ALL PARAMS!!!!!
        
        
        
        #need to cycle through all of the groupboxes
        
        for x in self.radio_screensizes:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedscreensize = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                filterby_screensize(self.warhouseitems, pickedscreensize)
                print(f"Filtering {pickedscreensize}")
                
            
    def getUsers_color(self):
        # THIS FUNCTION NEEDS TO CHECK ALL PARAMS!!!!!
        
        
        
        #need to cycle through all of the groupboxes
        
        for x in self.radio_color:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedscolor = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                filterby_color(self.warhouseitems, pickedscolor)
                print(f"Filtering {pickedscolor}")
      
    def getUsers_type_of_storage(self):
        for x in self.radio_storage:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedstorage = x.text()
                
                
                #this function is filtering by providing the processor inside of the application
                filterby_storagetype(self.warhouseitems, pickedstorage)
                print(f"Filtering {pickedstorage}")
        
        
        
        
        
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
            
    def mainfilter(self):
        
        for x in self.radio_storage:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedstorage = x.text()
                
        
        for x in self.radio_color:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedscolor = x.text()
                
        
        for x in self.radio_screensizes:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedscreensize = x.text()
                
                
        for x in self.radio_procesors:
            if x.isChecked():
                
                #works, stores a text of the processor
                pickedprocessor = x.text()
                
                
        
        storage = filterby_storagetype(self.warhouseitems,pickedstorage)
        color = filterby_color(self.warhouseitems,pickedscolor)
        screensize = filterby_screensize(self.warhouseitems,pickedscreensize)
        processor = filterby_proccesor(self.warhouseitems,pickedprocessor)
        
  

        intersection_set = set.intersection(set(storage), set(color),set(screensize), set(processor))
        intersection_list = list(intersection_set)
        #THIS IS IT THIS IS THE FUNCTION THAT IS RETURNING ALL OF THE FLTERED PRODUCTS 
        #FIX ====== if something is not chosen
        print("This is the result")
        print(intersection_list)  
        return intersection_list



#ALLOWS US TO ACTUALLY SEE THE MENU
#very important



#instance of the class




from registration import *
from PyQt5.QtWidgets import QMessageBox


if __name__ == "__main__":
        
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #instance of the class

    ui = firstApp(MainWindow)
    Everythingnew = []
    
    #FUNCTION THAT IS CALLING STUFF FROM VISUAL TO MAKE IT MORE CLEANER
    #1 to 5 means actually 1 to 4, limitation of for loop
    for x in range(1,5):  
        #Item = name
        #
        #x = iterator  
        
        #NEED TO THINK OF A WAY ON HOW TO ACTUALLY CONNECT FILTERED ELEMENTS TO THE GROUP BOXES
        IterationItems = ui.make_groupbox("Item","dopice",x)
        Everythingnew.append(IterationItems)
        
        
        
        
    print(Everythingnew)
    #calling the function to assign the buttons
    ui.hookupmainbuttons(Everythingnew)

    MainWindow.show()

    app.exec()

