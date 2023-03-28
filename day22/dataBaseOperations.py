#insert, update, delete

import mysql.connector
con=mysql.connector.connect(host="localhost", port=5432, user="Postgres", passwd="gauss1234567", database="Casts") #establish connection with the db
curs=con.cursor() #create cursor
curs.execute("") #execute query through through cursor
con.commit() #commit transaction
con.close()