import streamlit as st
import requests

# Streamlit UI
st.title('Prediction App')
st.write('Enter three numbers below:')

# User input fields
num1 = st.number_input('Number 1')
num2 = st.number_input('Number 2')
num3 = st.number_input('Number 3')

# Submit button
if st.button('Submit'):
    # Send user input to Flask API
    response = requests.post('http://localhost:5000/predict', json={'num1': num1, 'num2': num2, 'num3': num3})
    
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.write(f'Predicted Value: {prediction}')
    else:
        st.write('Error predicting value. Please try again.')
