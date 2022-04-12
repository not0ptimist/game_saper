"""CREATE DATABASE py_game_saper;
CREATE TABLE saper(
name VARCHAR(15) DEFAULT('gamer'),
secret_num INT,
result VARCHAR(15) NOT NULL);
"""
#Import the python driver for PostgreSQL
import psycopg2

#Create a connection credentials to the PostgreSQL database
try:
    connection = psycopg2.connect(
        user = "pyuser1",
        password = "pyuser1",
        host = "localhost",
        port = "5432",
        database = "py_game_saper"
    )

    #Create a cursor connection object to a PostgreSQL instance and print the connection properties.
    cursor = connection.cursor()
    # print(connection.get_dsn_parameters(),"\n")

    #Display the PostgreSQL version installed
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected into the - ' record,'\n")


    #Get the column name of a table inside the database and put some values
    pg_insert = """ INSERT INTO saper (name, secret_num, result)
                VALUES (%s,%s,%s)"""

    inserted_values = ('Johni', 39, 'BOOM')

    #Execute the pg_insert SQL string
    cursor.execute(pg_insert, inserted_values)

    #Commit transaction and prints the result successfully
    connection.commit()
    count = cursor.rowcount
    print (count, "Successfully inserted")


#Handle the error throws by the command that is useful when using python while working with PostgreSQL
except(Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL database", error)
    connection = None

#Close the database connection
finally:
    if(connection != None):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is now closed")