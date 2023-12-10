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
        for index, _ in enumerate(range(20), start=1):
            selected_number = random.choice(sept)
            selhour = random.choice(hour)
            minute = random.randint(1, 45)
            print(f"instance {index}: day {selected_number} hh:mm:ss {selhour} : {minute} : {minute}")
            datelog = "2023-9-" + str(selected_number) + " " + str(selhour) + ":" + str(minute) + ":" + str(minute)

            query0 = "SELECT * FROM serials order by rand() limit 1"
            query = "SELECT Date_Year, Volume,s.code,s.Date_Received, st.Serial_Title ,st.ISSN,st.Agent,Subject,s.volume , s.accession FROM serials as s left join serial_title as st on s.code = st.code WHERE RAND() <= 0.01 order by rand() limit 1"
            cursor.execute(query)
            rows = cursor.fetchall()
            #print(rows[0])

            if not rows:
                print(f"instance { index } empty" )
            else:
                try:
                    #print(f"instance { index } not empty")
                    columns = ('date_year',' copy',' kode',' Date_recieved',' title',' issn',' agent',' subject',' volume',' accession',' reg_date')
                    values = (rows[0][0], rows[0][1],rows[0][2],rows[0][3],rows[0][4],rows[0][5],rows[0][6],rows[0][7],rows[0][8],rows[0][9], datelog)
                    q =  f"INSERT INTO ssihs ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
                    ishcur.execute(q,values)
                    ishconn.commit()
                    print(f"instance { index } commit success")
                except ishconn.Error as err:
                    print(f"instance { index } commit error { err }")
                

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection when done
        close_mysql_connection(connection, cursor)
        ishclose(ishconn, ishcur)
        
