from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    weight = float(request.form['Weight'])
    length1 = float(request.form['Length1'])
    length2 = float(request.form['Length2'])
    length3 = float(request.form['Length3'])
    height = float(request.form['Height'])
    # width = float(request.form['Width'])  # Remove this if it's not used in the model

    # Create an array for prediction
    features = np.array([[weight, length1, length2, length3, height]])  # Ensure this matches the training features

    # Make prediction
    prediction = model.predict(features)

    # Render the result in the template
    return render_template('index.html', prediction_text=f'Predicted Fish Species: {prediction[0]}')

if __name__ == '__main__':
    app.run(port = 5001)
