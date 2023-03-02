import mysql.connector
try:
        conn = mysql.connector.connect(host = '127.0.0.1' , password = '' , user = 'root',database = 'flights')
        mycursor = conn.cursor()
        print('Connection Successful')
except Exception as e:
        print(e) 

mycursor.execute('''update flight set 
Destination = 'New Delhi',
Source = 'New Delhi' 
where Destination = 'Delhi' OR Source = 'Delhi'
''')
conn.commit()
print('commit successfull-1') 
mycursor.execute('''ALTER TABLE flight MODIFY COLUMN Route VARCHAR(255)''')
conn.commit()
print('commit successfull-2') 

