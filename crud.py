import mysql.connector 
try:
    conn = mysql.connector.connect(host = '127.0.0.1' , password = '' , user = 'root',database = 'indigo')
    mycursor = conn.cursor()
    print('Connection Successful')
except Exception as e:
    print(e)

# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# create a table  

# mycursor.execute('''
# CREATE TABLE airport (
#     airport_id INTEGER PRIMARY KEY ,
#     code VARCHAR(10) NOT NULL ,
#     city VARCHAR(255) NOT NULL ,
#     name VARCHAR(255) UNIQUE NOT NULL
# )
# ''')
# conn.commit()

# mycursor.execute('''
# INSERT INTO airport (airport_id , code , city , name) VALUES
# (1, 'DEL' , 'Delhi' ,'IGIA'),
# (2, 'KOL' , 'Kolkata' , 'NSCBA'),
# (3 , 'BOM', 'Mumbai' , 'CSIA')
# ''')
# conn.commit() 


# mycursor.execute('''
# SELECT * from airport where airport_id > 1
# ''')
# data = mycursor.fetchall()
# print(data)

# for i in data:
#     print(i[-1])

# update  

# mycursor.execute('''
# update airport set code = 'CAL' where airport_id = 2
# ''')
# conn.commit()

# delete from table  

mycursor.execute('''delete from airport where airport_id = 3''')
conn.commit()







