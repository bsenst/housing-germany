from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a function to perform the prediction
def predict_value(num1, num2, num3):
    # Perform prediction logic here
    # For this example, let's assume a simple sum of the three numbers as the prediction
    prediction = num1 + num2 + num3
    return prediction

# Define a route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    num3 = data['num3']
    
    prediction = predict_value(num1, num2, num3)
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
