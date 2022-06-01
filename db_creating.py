import psycopg2

import os
import sqlite3
from sqlite3 import Error





def initialize():
   if not os.path.exists('GreatBuy.db'):
        print('Create Database')
        connection = sqlite3.connect('GreatBuy.db')
        cursor = connection.cursor()
        create_workspace = '''  CREATE TABLE UserData(
            USER_ID TEXT PRIMARY KEY NOT NULL,
            PASSWORD TEXT,
            EMAIL TEXT,
            NAME TEXT
            
            
        ); 
        '''
        cursor.execute(create_workspace)
        connection.commit()
        connection.close()
