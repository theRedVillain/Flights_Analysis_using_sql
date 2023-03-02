import mysql.connector 

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = '127.0.0.1' , password = '' , user = 'root',database = 'flights')
            self.mycursor = self.conn.cursor()
            print('Connection Successful')
        except Exception as e:
            print(e)
    def fetch_flight_names(self):
        city = []
        self.mycursor.execute('''
        select distinct(Source) from flight 
        UNION 
        select distinct(Destination) from flight 
        ''')
        data = self.mycursor.fetchall()
        for i in data:
            city.append(i[0])
        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute(f'''
            SELECT Airline , Route , Dep_Time , Duration , Price from flight where Source = '{source}' and Destination = '{destination}'
        ''')

        result = self.mycursor.fetchall()

        return result 
    def airline_dist(self):
        self.mycursor.execute('''select Airline , COUNT(*) from flight group by Airline''')
        data = self.mycursor.fetchall()
        return data 

    def busy_count(self):
        self.mycursor.execute('''
        with cte as (
        SELECT Source , COUNT(*) as 'Freq' from flight group by Source 
        UNION 
        SELECT Destination , COUNT(*) as 'Freq' from flight group by Destination) 

        SELECT Source , SUM(Freq) from cte group by Source order by SUM(Freq) DESC
        ''') 

        data = self.mycursor.fetchall() 

        return data

    def flights(self):
        f_list = [] 
        self.mycursor.execute('''
        select DISTINCT(Airline) from flight
        ''')
        data = self.mycursor.fetchall()

        for i in data:
            f_list.append(i[0])
        return f_list

    def monthwise_flight(self,airline):
        self.mycursor.execute(f'''
        with cte as (
        select *, MONTHNAME(DATE(Date_of_Journey)) as 'Month_' from flight) 

        select cte.Month_,count(*) from cte where Airline LIKE '{airline}' group by cte.Month_;
        ''') 

        data = self.mycursor.fetchall() 
        return data 
    def total_travels(self):
        self.mycursor.execute('''
        with cte as (
        select *, MONTHNAME(DATE(Date_of_Journey)) as 'Month_' from flight) 

        select Month_ , count(*) as 'Total Flights'  from cte group by Month_ order by MONTH(DATE(Date_of_Journey)) asc 
        ''')

        data = self.mycursor.fetchall() 
        return data 