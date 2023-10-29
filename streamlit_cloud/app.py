import os.path
import pickle
import pandas as pd
from flask import Flask, request, jsonify
import streamlit as st
import requests

# load the pickled model file
if os.path.isfile("scripts/model.pkl"):
    model = pickle.load(open('scripts/model.pkl', 'rb'))
else:
    model = pickle.load(open('assets/model.pkl', 'rb'))

# Define a function to perform the prediction
def predict_value(noRoomsRange, livingSpaceRange):
    # create a dataframe with custom values
    custom_values = {'noRoomsRange': noRoomsRange, 'livingSpaceRange': livingSpaceRange}
    custom_df = pd.DataFrame(data=custom_values, index=[0])

    # predict using the loaded model and custom values
    prediction = model.predict(custom_df)

    return prediction

# Streamlit UI
st.title('Prediction App')
st.write('Enter three numbers below:')

# User input fields
noRoomsRange = st.number_input('noRoomsRange [binned noRooms]', min_value=1, max_value=5, value=3, step=1)
livingSpaceRange = st.number_input('livingSpaceRange [binned livingSpace]', min_value=1, max_value=7, value=4, step=1)

# Submit button
if st.button('Submit'):
    prediction = predict_value(noRoomsRange, livingSpaceRange)[0]

    st.write(f'Predicted baseRent: {round(prediction,1)}')
