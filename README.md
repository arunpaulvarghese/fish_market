This project is a web application that predicts the species of a fish based on its physical characteristics. The application uses a machine learning model trained on a dataset of fish measurements. The web interface allows users to input the fish's weight, length, height, and width, and then it predicts the species of the fish.



Features
User Interface: A simple web form to input fish measurements.
Machine Learning Model: A Random Forest classifier trained on the fish dataset.
Prediction Output: Displays the predicted fish species based on the input measurements.



Requirements
Python 3.6+
Flask
Scikit-learn
Pandas
Numpy
HTML & CSS for the front-end



Project Structure
index.html: HTML file for the web interface.
Fish_prediction.ipynb: Jupyter Notebook for training the machine learning model.
fish_prediction.py: Flask application for serving the web interface and making predictions.
classifier.pkl: Pickle file containing the trained Random Forest model.
fish.csv: Dataset used for training the model.




1. HTML File (index.html)
This file contains the structure of the web page, including a form where users can input the fish measurements and a button to submit the form. The form action is set to call the predict route in the Flask application.

2. Jupyter Notebook (Fish_prediction.ipynb)
Load the dataset and explore the data.
Split the data into independent (features) and dependent (target) variables.
Perform a train-test split to evaluate the model's performance.
Train a Random Forest classifier and evaluate its accuracy.
Save the trained model using the pickle module.
3. Flask Application (fish_prediction.py)
Initialize the Flask application.
Load the trained model from the pickle file.
Define the home route to render the index.html file.
Define the predict route to handle form submissions, make predictions, and return the prediction result to the user.
