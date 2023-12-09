import mysql.connector

def connect_to_mysql(host, user, password, database, port):
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

def close_mysql_connection(connection, cursor):
    # Close the cursor and connection when done
    if connection.is_connected():
        cursor.close()
        connection.close()
        #print("MySQL connection closed")


def decon(result, bago, huri):
    var1 = result.split(bago)
    var2 = var1[1].split(huri)
    var3 = var2[0].replace("\x1e", "")
    return var3


def makeDic(res):
    title = decon(res, "<001>", "<002>")
    author = decon(res, "<004>", "<005>") 
    barcode = decon(res, "<0026>", "<0027>")
    location = decon(res, "<0028>", "<0029>")  
    chold = decon(res, "<0025>", "<0026>") # 006.68
    cn = chold.split()
    if len(cn) == 4: #GC-ANT 301 S97 2004
        code1 = cn[0]
        call_number = cn[1]
        katers = cn[2]
        taon = cn[3]
        metadata = {
            "Title": title,
            "Author": author,
            "code1": code1,
            "call_number": call_number,
            "katers": katers,
            "taon": taon,
            "barcode": barcode,
            "location": location
        }

    elif len(cn) == 3:
        #print(cn)
        code1 = cn[0]
        call_number = ''
        katers = cn[1]
        taon = cn[2]      
        metadata = {
            "Title": title,
            "Author": author,
            "code1": code1,
            "call_number": call_number,
            "katers": katers,
            "taon": taon,
            "barcode": barcode,
            "location": location
        }
    
    else:
        metadata = {}
    
    
    return metadata