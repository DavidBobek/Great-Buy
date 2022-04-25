import psycopg2
from psycopg2 import Error

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
        PRUCE INT ,
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


""" import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database mydb''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close() """
