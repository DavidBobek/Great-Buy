import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    database='GreatBuy',
    user = 'postgres',
    password = 'postgres',

    
    
)



sql_query='''

    CREATE TABLE UserData(
        USER_ID TEXT PRIMARY KEY NOT NULL,
        PASSWORD TEXT,
        EMAIL TEXT
        NAME TEXT
        
        
    ); 

'''

pointer = con.cursor()


try:
    pointer.execute(sql_query)
    con.commit()
    print("Table created")
    
except:
    print("already created")

finally:
    con.close()