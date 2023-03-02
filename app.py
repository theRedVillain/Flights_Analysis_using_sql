import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from dbhelper import DB 
import plotly.graph_objects as go
import plotly.express as px
db = DB()
st.sidebar.title('Flight Analytics')
user_selection = st.sidebar.selectbox('Menu',['Home','Check Flights','Analytics'])

if user_selection == 'Home':
    st.title('Hello, ')
    para = '''
    Welcome to our Flight Analytics application! Our platform provides you with valuable insights on the flight industry, including the number of flights, prices, destinations, and other general trends. Whether you're a frequent traveler or simply curious about the aviation industry, our app offers a comprehensive look into the latest data and trends in the market. With easy-to-use tools and real-time updates, you can quickly and easily access the information you need to make informed decisions about your travel plans. So why wait? Start exploring today and gain a better understanding of the flight industry!
    ''' 
    st.write(para)
elif user_selection == 'Check Flights':
    st.title('Check Flights')
    city = db.fetch_flight_names()
    col1,col2 = st.columns(2)
    with col1:
        station1  = st.selectbox('From',city,key = 'u1')
    with col2:
        station2 = st.selectbox('To',city[::-1],key = 'u2')
    if station1 == station2 :
        st.error('Error! Chhote ache se Kaam Kar')
    if st.button('Search Flights'):
        result = db.fetch_all_flights(station1 , station2)
        df = pd.DataFrame(result,columns = ['Airline','Routes','Departure','Duration','Price'])
        df['Routes'] = df['Routes'].replace('â†’','->')
        st.dataframe(df)

else:
    st.title('Insights')
    st.subheader('Distribution of Flights : ')
    df = pd.DataFrame(db.airline_dist() , columns = ['Airline','Operating Freq'])

    keys = df['Airline']
    Values = df['Operating Freq']

    fig = go.Figure(data=[go.Pie(labels=keys, values=Values)])

    fig.update_layout(
    title="Distribution",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
    )  
    st.plotly_chart(fig) 


    st.subheader('Arranging Airport on the basis of busyness level : ') 

    df = pd.DataFrame(db.busy_count(), columns = ['Airport','Count of Flights'])
    df['Count of Flights'] = df['Count of Flights'].astype(int)
    st.bar_chart(df.set_index('Airport'))

    st.subheader('Month Wise Distribution for Particular Flights : ')
    airline = db.flights()
    u_input = st.selectbox('Select a Airline',airline)
    db_ = pd.DataFrame(db.monthwise_flight(u_input) ,columns = ['Month','Number_of_Flights'])
    st.dataframe(db_ , width = 750)
    st.bar_chart(db_.set_index('Month'))
    
    st.subheader('Total Flights Month Wise : ')
    my_df = pd.DataFrame(db.total_travels(),columns = ['Month','Total Travels'])

    fig_ = px.line(my_df , x = 'Month' , y = 'Total Travels')
    st.plotly_chart(fig_)
    