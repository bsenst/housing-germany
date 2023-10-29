import streamlit as st
import requests

# Streamlit UI
st.title('Prediction App')
st.write('Enter three numbers below:')

# User input fields
noRoomsRange = st.number_input('noRoomsRange [binned noRooms]', min_value=1, max_value=5, value=3, step=1)
livingSpaceRange = st.number_input('livingSpaceRange [binned livingSpace]', min_value=1, max_value=7, value=4, step=1)

# Submit button
if st.button('Submit'):
    # Send user input to Flask API
    response = requests.post('http://localhost:5000/predict', json={'noRoomsRange': noRoomsRange, 'livingSpaceRange': livingSpaceRange})
    
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.write(f'Predicted baseRent: {round(prediction,1)}')



    else:
        st.write('Error predicting value. Please try again.')
