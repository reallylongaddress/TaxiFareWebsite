#from turtle import onclick
import streamlit as st
import datetime
import requests

def run_query(get_params):

    url = 'https://taxifare.lewagon.ai/predict'
    res = requests.get(url, params=get_params)
    fare_estimate = round(res.json().get('fare'), 2)
    st.write('fare_estimate:', fare_estimate)



pickup_date = st.date_input('Pickup date:', datetime.date(2019, 7, 6))
pickup_time = st.time_input('Pickup time: ', datetime.time(8, 45))
pickup_lat = st.text_input('Pickup Latitude', '40.775069')
pickup_lon = st.text_input('Pickup Longitude', '73.87071')
dropoff_lat = st.text_input('Dropoff Latitude', '40.642422')
dropoff_lon = st.text_input('Dropoff Longitude', '73.781749')
passenger_count = st.selectbox('Num Passengers?', ('1', '2', '3'))

get_params = {
    "pickup_latitude": pickup_lat,
    "pickup_longitude": pickup_lon,
    "dropoff_latitude": dropoff_lat,
    "dropoff_longitude": dropoff_lon,
    "passenger_count": passenger_count,
    "pickup_datetime": f'{pickup_date} {pickup_time}',

}

st.button('Run Prediction', on_click=run_query(get_params))

# st.write('--------------------')
# st.write('Pickup date: ', pickup_date)
# st.write('Pickup time: ', pickup_time)
# st.write('The current pickup latitude is: ', pickup_lat)
# st.write('The current pickup Longitude is: ', pickup_lon)
# st.write('The current dropoff latitude is: ', dropoff_lat)
# st.write('The current dropoff Longitude is: ', dropoff_lon)
# st.write('Number passengers:', passenger_count)
