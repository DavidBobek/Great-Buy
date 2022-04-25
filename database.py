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

    

    connection.commit()

    print("Table was created")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


