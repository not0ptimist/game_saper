import psycopg2


# Connect to an existing database
# conn = psycopg2.connect("dbname=test1 user=postgres")
try:
    connection = psycopg2.connect(
        user = "pyuser1",
        password = "pyuser1",
        host = "localhost",
        port = "5432",
        database = "py_game_saper"
    )

    # Open a cursor to perform database operations
    cur = connection.cursor()

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO test1 (name, date_time, result) VALUES (%s, %s, %s)",
                ("Mike", "1999-01-08 04:12:45", "0"))

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test1;")
    tabl = cur.fetchmany(10)
    for i in tabl:
        print(i)
    # (1, 100, "abc'def")

    # Make the changes to the database persistent
    connection.commit()

#Handle the error throws by the command that is useful when using python while working with PostgreSQL
except(Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL database", error)
    connection = None

#Close the database connection
finally:
    if(connection != None):
        cur.close()
        connection.close()
        print("PostgreSQL connection is now closed")