from View_Item import View_Item_UI
from product import Basket
from user import User
import re
import smtplib
from smtplib import SMTP
from registration import *
import sys
from db_creating import *


# validation of the inputs from registration
def validation(name, email_address, password):
    correctness = 1
    if not name.isalpha():
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
    



def filterby_proccesor(warehouse, users_choice):
    """ 
    warehouse: List of all items
    users_choice: value of a function "getUsers_processor()"
                : type(dictionary) 
                : {"processor",processor_value}
    """
    final = []
    for x in warehouse:
        #checking if the choice is empty
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
    """ 
    warehouse: List of all items
    users_choice: value of a function "getUsers_screensize()"
                : type(dictionary) 
                : {"screensize",screensize_value}
    """
    
    # Categories of the screens
    smallest = []
    lowmid = []
    mid = []
    high_mid = []
    high = []
    
    
    final = []
    #for loop that asssigns products to categories
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

    #manager of returning the correct type
    if users_choice == {'screensize': 'x<11"'}:     
        return smallest
    
    if users_choice == {'screensize': '11\'\'≥x<14"'}:      
        return lowmid
    
    if users_choice =={'screensize':  '14"≥x<15.6"'}:
        return mid
    
    if users_choice =={'screensize':  '15.6\'\'≥x<17.3"'}:  
        return high_mid
    
    if users_choice == {'screensize': 'x≥17.3"'}:
        return high
    
    if users_choice == {}:
        return final
    
  
    

def filterby_color(warehouse,users_choice): 
    """ 
    warehouse: List of all items
    users_choice: value of a function "getUsers_color()"
                : type(dictionary) 
                : {"color",color_value}
    """
    
    final = []

    for x in warehouse:
        if users_choice == {}:
            return final
        if x.color == users_choice["color"]:
            final.append(x)

    #error handling
    if len(final) == 0:
        return final
    else:
        return final



def filterby_storagetype(warehouse, users_choice):
    """ 
    warehouse: List of all items
    users_choice: value of a function "getUsers_type_of_storage"
                : type(dictionary) 
                : {"storage_type",storage_value}
    """
    final = []
    #this actually might be the final solution
    for x in warehouse:
        if users_choice == {}:
            return final
        if x.storage_type == users_choice["storage_type"]:
            final.append(x)
        else:
            pass
        
    # Error handling
    if len(final) == 0:
        return final
    else:
        return final



from Visual import *
from items import Scrolling
import sys
import database
from checkout import Checkout_window
from warehouse_products import *
from login import login_ui
class firstApp(Ui_MainWindow):
    """ 
    Instance of a class firstApp
    """
    
    def __init__(self,window):      
        self.setupUi(window)
        """ 
        Connecting the main buttons to the respective functions
        
        """
        self.filter_button.clicked.connect(self.getUsers_processor)
        self.filter_button.clicked.connect(self.getUsers_sizes)
        self.filter_button.clicked.connect(self.getUsers_color)
        self.filter_button.clicked.connect(self.getUsers_type_of_storage)
        self.filter_button.clicked.connect(self.mainfilter)
        self.clear_button.clicked.connect(self.clear    )
        self.login_button.clicked.connect(self.openregistration)
        self.register_button.clicked.connect(self.openlogin)
        
        self.shopping_button.clicked.connect(lambda:self.opencheckout(current_basket))
        

        """
        Creation of parameters and assigning the various inputs 
        """
        self.radio_procesors = [self.Intel_9,self.Intel_7,self.Intel_5,self.Intel_3,self.AMD5,self.AMD7,self.AMD9]
        self.radio_screensizes = [self.smallest,self.lowermid,self.mid,self.uppermid,self.largest]
        self.radio_color = [self.c_black,self.c_silver,self.c_white,self.c_gray]  
        self.radio_storage = [self.storage_ssd,self.storage_HDD]
    

    
        
        """
        the variable warhouseitems is being passed passed from a foreign file <warehouseproducts.py"
        """
        self.warhouseitems = allitems

    def openregistration(self):
        """
        Function is responsible for opening a new window whenever user decides to register 
        """
     
        self.window = QtWidgets.QMainWindow()
        self.ui = Registration_Ui()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.proceed_button.clicked.connect(self.checking)
        
        
    def openlogin(self):
        """
        Function is responsible for opening a new window whenever user decides to login 
        """
     
        self.window = QtWidgets.QMainWindow()
        self.ui = login_ui()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.proceed_button.clicked.connect(self.login)
        
        
    def opencheckout(self,basket):    
        """
        basket: instance of object Basket
              : type(basket.items) = dictionary 
        Function is responsible for opening a paying window 
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = Checkout_window()
        self.ui.setupUi(self.window)
        self.window.show()
        #adding every item in the basket to a combo box for a review
        for x in basket.items:
            self.ui.comboBox.addItem(x.name)
        
        self.ui.total_price_text.setText(f'{str(basket.calculate_total_value())} €')
        self.ui.pay_button.clicked.connect(ui.pay)
        
        
    def login(self):
        """
        whenever a user decides to login he/she is presented
        """
 
        email = self.ui.email_entry.text()
        password = self.ui.password_entry.text()
        
        data = database.login(email,password)
        
        if data == []:
            self.ui.email_entry.setText("")
            self.ui.password_entry.setText("")
            
        else:
            data = data[0]
            print("The user has logged in")
            global newUser
            newUser = User(id=data[0],password=data[1],email=data[2],name=data[3])
            self.window.hide()
            
    
    
        
    


    def pay(self):
        #maybe write something into another database
        
   
        """
           body = f'Hi {name}! This is a AllBuy!\nCongratulation with your purchase. You have bought: {out[:-2]}\nThe total price would be {price} {currency}'

            msg = f'Subject: {subject}\n\n{body}'

            server.sendmail('allbuyco2022@gmail.com', f'{email}', msg)
        """
        try:
            
            
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                try:
                    
                    products = """"""
                    for x in newUser.basket.items:
                        
                        product= """"""
                        product += "\n"
                        product += f'Name: {x.name}'
                        product += "\n"
                        product += f'Processor: {x.processor}'
                        product += "\n"
                        product += f'Storage Type: {x.storage_type}'
                        product += "\n"
                        product += f'Price: {x.price}'
                        product += "\n"
                        product += f'Color: {x.color}'
                        product += "\n"
                        product += f'Screen size: {x.screensize}'
                        product += "\n"
                        product += f'Description: {x.description}'
                        product += "\n"
                        product += f'Product Price: {x.price}'
                        product += "\n"
                        product += "\n"
                        
                        products += product
                        
                        
                        #ll = [f'{name}={value}\n' for name, value in x._dict_.items()]
                    server.login('greatbuyeshop@gmail.com', 'hufgoexbthpcfhew')
                    
                    subject = 'GreatBuy: Your order'
                    body = f'''Thank you {newUser.name} for buying the products with a value of {current_basket.calculate_total_value()} euros
                    
                    The products you have bought are: 
{products}'''
                    msg = f'Subject: {subject}\n\n{body}'
                    
                    server.sendmail('greatbuyeshop@gmail.com',newUser.email,msg)
                    print("payed")
                    self.window.hide()
                    
        
                except smtplib.SMTPAuthenticationError as error:
                    print(f'Something is wrong with sender data {error}')     
        except:
            self.openregistration()
            
        """ def email_verification(name, email, code):
    

    :param name: user_name
    :param email: user_email
    :param code: randomly generated to verify email
    :return: sends email to mentioned email address with the code in order to verify if this email belongs to our user
   
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        try:
            server.login('allbuyco2022@gmail.com', 'onxvgueeekrealob')

            subject = 'Verify Email Address'
            body = f'Hi {name}! This is a AllBuy!\n\tThis is a verification message. Your code is: {code}.'

            msg = f'Subject: {subject}\n\n{body}'

            server.sendmail('allbuyco2022@gmail.com', f'{email}', msg)
        except smtplib.SMTPAuthenticationError as error:
            print(f'Something is wrong with sender data {error}')"""
            
            
    def checking(self):
        
        """
        Function is responsible for a final checking before writing into a database 
        """
        entry_name = self.ui.name_entry.text()
        entry_email = self.ui.email_entry.text()
        entry_password = self.ui.password_entry.text()
        
        
        if validation(entry_name,entry_email,entry_password) == "Valid" and self.ui.age_check.isChecked():
            if database.controlling(entry_email) == "Not":    
                global newUser
                newUser = User(entry_name,entry_email,entry_password)
                #writing into a database
                database.registering(newUser)
                print("User registered")
                self.window.hide()
                
            
                
            else:
                self.ui.name_entry.setText("User with this email adress already exists")
                self.ui.email_entry.setText("User with this email adress already exists")
                self.ui.password_entry.setText("User with this email adress already exists")
                
            
        else:
            self.ui.name_entry.setText("")
            self.ui.email_entry.setText("")
            self.ui.password_entry.setText("")
    
    
        
    
    def getUsers_processor(self):
        """ 
        Function responsible for looping through entry boxes and gathering the final output
        return: final_result
              : type(final_result) = dictionary
              : {"processor",pickedprocessor}
        """
    
        for x in self.radio_procesors:
            if x.isChecked():                              
                pickedprocessor = x.text()      
                final_result = {"processor":pickedprocessor}
                return final_result
        return {}
               
                
    def getUsers_sizes(self):
        """ 
        Function responsible for looping through entry boxes and gathering the final output
        return: final_result
              : type(final_result) = dictionary
              : {"screensize",pickedscreensize}
        """
    
        for x in self.radio_screensizes:
            if x.isChecked():  
                pickedscreensize = x.text()
                final_result = {"screensize":pickedscreensize}
                return final_result
        return {}
    def getUsers_color(self):
        """ 
        Function responsible for looping through entry boxes and gathering the final output
        return: final_result
              : type(final_result) = dictionary
              : {"color",pickedcolor}
        """
    
        for x in self.radio_color:
            if x.isChecked():     
                pickedscolor = x.text()    
                final_result = {"color":pickedscolor}
                return final_result
        return {}
      
    def getUsers_type_of_storage(self):
        """ 
        Function responsible for looping through entry boxes and gathering the final output
        return: final_result
              : type(final_result) = dictionary
              : {"storage_type",pickedstorage}
        """
        
        for x in self.radio_storage:
            if x.isChecked():             
                pickedstorage = x.text()   
                final_result = {"storage_type":pickedstorage}
                return final_result
        return {}
        

        
    #popping up a new window          
    def View_more(self,items,pos):
        """ 
        Function that is activated when a user decides to inspect an item
        items: dictionary of all filtered items
             : {index,[item]}
        pos: position of the item we are selecting (integer) 
        
        """
        
        
        
        item = items[pos][0]
        self.window = QtWidgets.QMainWindow()
        self.ui = View_Item_UI()   
        self.ui.setupUi(self.window)
        self.ui.button_add_to_cart.clicked.connect(lambda: ui.add_to_cart(item))     
        _translate = QtCore.QCoreApplication.translate
        #specifiing the paramaters passed from the item
        self.ui.label_Color.setText(_translate("MainWindow", item.color))
        self.ui.label_Name.setText(_translate("MainWindow", item.name))
        self.ui.label_price.setText(_translate("MainWindow",f' {str(item.price)} €'))
        self.ui.label_processor.setText(_translate("MainWindow", item.processor))
        self.ui.label_storage.setText(_translate("MainWindow", item.storage_type))
        self.ui.label_about.setText(_translate("MainWindow", item.description))
        self.ui.label_screensize.setText(_translate("MainWindow", item.screensize))
        
        self.window.show()
        
    def add_to_cart(self,item):
        """ 
        Function that is putting an item into the basket
        item: instance of an object Product
        """
        
        try:
            newUser.assignbasket(current_basket)
        except:
            
            stock_user.assignbasket(current_basket)
        current_basket.additem(item)
        print("Added to cart")
            
    def hook_item_functions(self,widgets,_items):
        """
        Function that is responsible to correctly assigning the function View_more
        I have chosen this approach because the function View_more must work differently for each
        product. Iam using the lambda function in order to be able to pass parameters 
        widgets: consist of all the elements that are going to be displayed
        _items: items that have been filtered
        """
        
        counting = 0
        
        
        for x in range(len(widgets.button_list)):
            if counting< len(_items):
                widgets.button_list[x].clicked.connect(lambda ch, x=x: self.View_more(_items,x))
                counting += 1

        counter = 0
        #assigning names to labels that have been filtered
        #I have opted for the most important parameters of a computer
        for x in widgets.Labellist:
            
            x.setText(f"Processor: {_items[counter][0].processor}, Brand: {_items[counter][0].brand}, Price: {_items[counter][0].price} €")
            counter += 1
    

    def clear(self):
        """
        The function clear gathers all of the radio buttons and unchecks all of them 
        """
        radio_buttons = self.radio_procesors+self.radio_screensizes+self.radio_color+self.radio_storage
        for x in radio_buttons:
            if x.isChecked():
                x.setAutoExclusive(False)
                x.setChecked(False)
                x.setAutoExclusive(True)
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
        
        if storage_pick:
            Not_null_params.append("storage_type")
            
        
        if color_pick:
            Not_null_params.append("color")
            
        
        if processor_pick:
            Not_null_params.append("processor")
            
        
        if screensize_pick:
            Not_null_params.append("screensize")
            

        

        
        filtered_elements = []
        #final products is a list of items to which iam going to be appending correctly filtered items
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
                    my_Category =  'x<11"'
                
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
                    
            #appending process
            #The program is controlling and checking all of the paramets have been fullfilled
            if (fav_color == {} or fav_color.get("color") == x.color) and  (fav_processor == {} or fav_processor.get("processor") == x.processor) and (fav_storage == {} or fav_storage.get("storage_type") == x.storage_type)  and (my_Category == {} or my_Category==fav_size.get("screensize")):
                final_products.append(x)
        
        print("\n")
        
        #activating the function View_items that opens a window with all the filtered items
        self.View_items(final_products)
        return final_products

    def View_items(self,_items):
        """
        Function View_items is responsible for displaying a filtered items
        _items: is a list hold the items
        """
        self.window = QtWidgets.QMainWindow()
        self.scroll = Scrolling(_items)
        
        
        """ 
        items_dic: is a dictionary hold the items
              : {index,[item]} """
        items_dic = {}
        for x in range(len(_items)):
            items_dic[x] = [_items[x]] 
            
        #after conversion to a dictionary we are activating the function hook_item_functions() that assigns the buttons to a function
        ui.hook_item_functions(self.scroll,items_dic)
       

#instance of the class


start = 0
while start == 0:
    start = 2
    initialize()
    
    stock_user = User("defualt","default@mail.com","adminADMIN1")
    current_basket = Basket()
        
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #instance of the class

    ui = firstApp(MainWindow)
    Everythingnew = []

    MainWindow.show()

    app.exec()
   
