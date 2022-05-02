import psycopg2


from user import User


davidko = User("davidko","dbobo","1234234",123)

def registering(user):
    con = psycopg2.connect(
    host = 'localhost',
    database='GreatBuy',
    user = 'postgres',
    password = 'postgres',

    
    )
    _id = f'\'{user.id}\''
    password = f'\'{user.name}\''
    email = f'\'{user.email}\''

    insert_sql_query = f'''

    INSERT INTO UserData(USER_ID,PASSWORD,EMAIL)VALUES ({_id}, {password}, {email});;



    '''
    
    pointer = con.cursor()
    pointer.execute(insert_sql_query)
    print("Data inputted")
    
    

    con.commit()
    con.close()
    
    



registering(davidko)