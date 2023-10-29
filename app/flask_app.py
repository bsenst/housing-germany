import os.path
import pickle
import pandas as pd
from flask import Flask, request, jsonify

# load the pickled model file
if os.path.isfile("scripts/model.pkl"):
    model = pickle.load(open('scripts/model.pkl', 'rb'))
else:
    model = pickle.load(open('assets/model.pkl', 'rb'))

app = Flask(__name__)

# Define a function to perform the prediction
def predict_value(noRoomsRange, livingSpaceRange):
    # create a dataframe with custom values
    custom_values = {'noRoomsRange': noRoomsRange, 'livingSpaceRange': livingSpaceRange}
    custom_df = pd.DataFrame(data=custom_values, index=[0])

    # predict using the loaded model and custom values
    prediction = model.predict(custom_df)

    return prediction

# Define a route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    noRoomsRange = data['noRoomsRange']
    livingSpaceRange = data['livingSpaceRange']
    
    prediction = predict_value(noRoomsRange, livingSpaceRange)[0]
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
