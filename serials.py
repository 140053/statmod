
import random
from pprint import pprint

from db.ihsdb import *
from db.pmasterdb import *

if __name__ == "__main__":
    # Replace these values with your actual database credentials
    host = "localhost"
    user = "root"
    password = "140053ken"
    database = "db_a84cf7_cbsua"
    database2 = "webopacwihs"
    port = "3306"

    # Establish connection
    connection, cursor = connect_to_mysql(host, user, password, database, port)
    ishconn , ishcur = ishcon(host, user, password, database2, port)


    sept = [1,4,5,6,7,8,11,12,13,14,18,19,20,21,25,26,27,28,29]
    october = [2,3,4,5,6,9,10,11,12,13,16,17,18,19,20,23,24,25,26,27,30,31]
    november = [3,6,7,8,9,10,13,14,15,16,17,20,21,22,23,24,28,29,30]
    hour = [7,8,9,10,11,12,13,14,15]
    
 

    try:
        for index, _ in enumerate(range(1), start=1):
            selected_number = random.choice(november)
            selhour = random.choice(hour)
            minute = random.randint(1, 45)
            print(f"month {index}: day {selected_number} hh:mm:ss {selhour} : {minute} : {minute}")
            datelog = "2023-11-" + str(selected_number) + " " + str(selhour) + ":" + str(minute) + ":" + str(minute)

            # Example: Execute a simple query
            query0 = "SELECT * FROM db_a84cf7_cbsua.serials AS s JOIN db_a84cf7_cbsua.serial_title AS st ON s.code = st.code WHERE RAND() <= 0.01 ORDER BY RAND()  LIMIT 1;"
            query = "SELECT Date_Year,Volume,serials.Code,serials.accession,Serial_Title,ISSN,Agent,Subject FROM serials left join  serial_title on serials.code = serial_title.code limit 1;"
            cursor.execute(query)

            # Check if there are any rows
            if cursor.rowcount > 0:
                # Fetch all rows
                rows = cursor.fetchall()
                print(rows)
            else:
                print("No rows found.")

    except Exception as e:
        print(f"Error: {e}")

            #rec1 = makeDic(rows[0][0])    
            #print(rec1['Title'])  #to insert 
            #{'Title': 'Planned change in farming systems: progress in on-farm research', 'Author': '', 'code1': 'GC-FMS', 'call_number': '630.72', 'katers': 'P6933', 'taon': '1991', 'barcode': 'MLIB00017655', 'location': 'GC-FMS - Circulation'}
            #if not rec1:
            #    print("metadata is empty")
            #else:
            #    q = "INSERT INTO ihubk (title, author, code1, call_number, katers, taon, barcode, location, reg_date ) VALUES ('"+ rec1['Title'] + "', '"+rec1['Author'] + "', '"+rec1['code1']+ "', '"+rec1['call_number']+ "', '"+rec1['katers']+ "', '"+rec1['taon']+ "', '"+rec1['barcode']+ "','"+rec1['location'] + "', '"+datelog+"');"
                #print(q)
            #    ishcur.execute(q)
            #    ishconn.commit()


    finally:
        # Close the cursor and connection when done
        close_mysql_connection(connection, cursor)
        ishclose(ishconn, ishcur)


    
