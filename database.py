
import sqlite3
from unicodedata import name
import psycopg2


from user import User




def registering(user):
    con = sqlite3.connect(
        'GreatBuy.db'
    )
    pointer = con.cursor()
    _id = f'\'{user.id}\''
    password = f'\'{user.password}\''
    name = f'\'{user.name}\''
    email = f'\'{user.email}\''

    insert_sql_query = f'''

    INSERT INTO UserData(USER_ID,PASSWORD,EMAIL,NAME)VALUES ({_id}, {password}, {email}, {name});
    
    '''
    
    con.commit()
    pointer.execute(insert_sql_query)
    
    print("Data inputted")
    
    

    con.commit()
    con.close()
    
    
def login(email,password):
    con = sqlite3.connect(
        'GreatBuy.db'
    )

    password = f'\'{password}\''
    email = f'\'{email}\''

    insert_sql_query = f'''

    SELECT * FROM UserData WHERE EMAIL = {email} and PASSWORD = {password};


    '''
    
    pointer = con.cursor()
    pointer.execute(insert_sql_query)
    user_data = pointer.fetchall()

    
    
    

    

    return user_data
def controlling(email):
    con = sqlite3.connect(
        'GreatBuy.db'
    )
    
    insert_sql_query = '''

    SELECT * FROM UserData;



    '''
    
    pointer = con.cursor()
    pointer.execute(insert_sql_query)
    
    user_data = pointer.fetchall()  # searches for user
    for x in user_data:
        if x[2] == email:
            return "Found"
    
    else:
        return "Not"
        
    

def deleting():
    con = sqlite3.connect(
        'GreatBuy.db'
    )
    
    insert_sql_query = '''

    DELETE FROM UserData ;



    '''
    
    pointer = con.cursor()
    pointer.execute(insert_sql_query)
    print("done")
    
    con.commit()
    con.close()
    
#deleting()\
  
