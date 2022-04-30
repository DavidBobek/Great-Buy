import psycopg2
from psycopg2 import Error
#from config import config

# fix line 9 CONNECTION NOT DEFINED

#david
#postgresdb
try:

    connection = psycopg2.connect(
        user="postgres",
        password="postgresdb",
        host="127.0.0.1",
        port="5433",
        database="postgres",
    )

    cursor = connection.cursor()

    # SQL query to create a BRAND NEW TABLE

    create_table = """ CREATE TABLE userinfo(
        USER_ID INT PRIMARY KEY NOT NULL,
        PRODUCT_ID INT NOT NULL,
        PRICE INT ,
        TIME DATE);"""

    # EXECUTING the creation of database

    cursor.execute(create_table)

    connection.commit()

    print("Table was created")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
    
    try:
        #figure out how to add just admin, data
        pass
    
    except:
        pass


finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
        
        



###WORK ON THIS

mydb = psycopg2.connect(
  host="localhost",
  user="postgres",
  password="postgresdb",
  database="postgres"
)

mycursor = mydb.cursor()



def dbInsert(payload):
    
    sql = "INSERT INTO user_info (USER_ID,PRODUCT_ID,PRICE,TIME) VALUES (%i, %s, %s, %s)"
    val = (payload[0], payload[1], payload[2], payload[3])
    mycursor.execute(sql, val)
    mydb.commit()
    
    
    
dbInsert([1,1,1])