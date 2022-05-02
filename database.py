import psycopg2


from user import User




def registering(user):
    con = psycopg2.connect(
    host = 'localhost',
    database='GreatBuy',
    user = 'postgres',
    password = 'postgres',

    
    )
    _id = f'\'{user.id}\''
    password = f'\'{user.password}\''
    email = f'\'{user.email}\''

    insert_sql_query = f'''

    INSERT INTO UserData(USER_ID,PASSWORD,EMAIL)VALUES ({_id}, {password}, {email});;



    '''
    
    pointer = con.cursor()
    pointer.execute(insert_sql_query)
    print("Data inputted")
    
    

    con.commit()
    con.close()
    
    

def controlling(id):
    con = psycopg2.connect(
    host = 'localhost',
    database='GreatBuy',
    user = 'postgres',
    password = 'postgres',
    )
    
    insert_sql_query = f'''

    SELECT * FROM UserData WHERE USER_ID = {id};



    '''
    
    pointer = con.cursor()
    pointer.execute(insert_sql_query)
    

def deleting():
    con = psycopg2.connect(
    host = 'localhost',
    database='GreatBuy',
    user = 'postgres',
    password = 'postgres',
    )
    
    insert_sql_query = '''

    DELETE FROM UserData ;



    '''
    
    pointer = con.cursor()
    pointer.execute(insert_sql_query)
    print("done")
    
    con.commit()
    con.close()
    
deleting()

#registering(davidko)