import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk

st.set_page_config(page_title="Ultimate Car Resale Value", page_icon="🚗", layout="wide")

model = pk.load(open('modelfinal.pkl', 'rb'))
cd = pd.read_csv('2.csv')

def get(car_name):
    return car_name.split(' ')[0].strip()

def clean(value):
    if isinstance(value, str):
        value = value.split(' ')[0].strip()
    return float(value) if value != '' else 0

cd['name'] = cd['name'].apply(get)
cd['mileage'] = cd['mileage'].apply(clean)
cd['engine'] = cd['engine'].apply(clean)
cd['max_power'] = cd['max_power'].apply(clean)

st.markdown("""
    <style>
        .custom-container {
            background-color: #EAEDED;
            padding: 20px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 30px;
        }

    </style>
""", unsafe_allow_html=True)

st.markdown('''
    <div class="custom-container">
        <span style="font-size: 50px; font-weight: bold; color: #2C3E50;">🚗 Estimate Your Wheels</span>
    </div>
''', unsafe_allow_html=True)

st.write("### Input Car Details")
col1, col2, col3, col4 = st.columns(4)

with col1:
    name = st.selectbox('Car Brand', cd['name'].unique(), key='name')
    fuel = st.selectbox('Fuel Type', cd['fuel'].unique(), key='fuel')
    max_power = st.slider('Max Power (bhp)', 0, 200, key='max_power')

with col2:
    color = st.selectbox('Car Color', cd['Color'].unique(), key='color')
    seats = st.selectbox('Number of Seats', [5, 6, 7, 8, 9, 10], key='seats')
    engine = st.slider('Engine (cc)', 700, 5000, key='engine')

with col3:
    seller_type = st.selectbox('Seller Type', cd['seller_type'].unique(), key='seller_type')
    transmission = st.selectbox('Transmission Type', cd['transmission'].unique(), key='transmission')
    km_driven = st.slider('KMs Driven', 0, 200000, key='km_driven')

with col4:
    owner = st.selectbox('Owner Type', cd['owner'].unique(), key='owner')
    year = st.number_input('Manufacturing Year', min_value=1994, max_value=2024, step=1, value=2024, key='year')
    mileage = st.slider('Mileage (km/l)', 10, 40, key='mileage')

st.write("### Upload Car Views")
image_col1, image_col2 = st.columns(2)

with image_col1:
    front_view = st.file_uploader("Upload Front View", type=["jpg", "jpeg", "png"], key="front_view")

    side_view_1 = st.file_uploader("Upload Side View 1", type=["jpg", "jpeg", "png"], key="side_view_1")

with image_col2:
    back_view = st.file_uploader("Upload Back View", type=["jpg", "jpeg", "png"], key="back_view")

    side_view_2 = st.file_uploader("Upload Side View 2", type=["jpg", "jpeg", "png"], key="side_view_2")

if st.button("Predict Car Price", key="predict"):
    with st.spinner('Estimating the car price...'):
        input_data = pd.DataFrame([[
            name, year, km_driven, fuel, seller_type, transmission, owner,
            mileage, engine, max_power, seats, color
        ]], columns=['name', 'year', 'km_driven', 'fuel', 'seller_type',
                     'transmission', 'owner', 'mileage', 'engine',
                     'max_power', 'seats', 'Color'])

        input_data['owner'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
        input_data['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
        input_data['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
        input_data['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
        input_data['name'].replace(cd['name'].unique(), range(1, len(cd['name'].unique()) + 1), inplace=True)
        input_data['Color'].replace(cd['Color'].unique(), range(1, len(cd['Color'].unique()) + 1), inplace=True)

        car_price = model.predict(input_data)
        st.success(f'Estimated Car Price: **₹{car_price[0]:,.2f}**')
