from flask import Flask, request, render_template
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Initialize the Flask app
app = Flask(__name__)

# Load model and scaler (assuming you've saved them after training)
with open("logistic_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    open_price = float(request.form['Open'])
    high_price = float(request.form['High'])
    low_price = float(request.form['Low'])
    close_price = float(request.form['Close'])
    adj_close_price = float(request.form['Adj Close'])
    volume = int(request.form['Volume'])

    # Scale input data
    input_data = np.array([[open_price, high_price, low_price, close_price, adj_close_price, volume]])
    scaled_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_data)

    # Interpret prediction
    result = "Increase" if prediction[0] == 1 else "Decrease"

    return render_template('index.html', prediction_text=f'Prediction: Stock price will {result} next day.')

if __name__ == '__main__':
    app.run(debug=True)
