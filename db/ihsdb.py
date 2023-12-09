import mysql.connector

def ishcon(host, user, password, database, port):
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            #print("Connected to the MySQL database")

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            return connection, cursor

    except mysql.connector.Error as e:
        print(f"Error: {e}")

def ishclose(connection, cursor):
    # Close the cursor and connection when done
    if connection.is_connected():
        cursor.close()
        connection.close()
        #print("MySQL connection closed")

