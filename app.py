from flask import Flask, request, app, render_template
import numpy as np
import pickle

app = Flask(__name__)                               # Initializing the flask app
model = pickle.load(open('model.pkl', 'rb'))       # Loading the model

@app.route('/')                                     # Defining the home page of our web-app
def home():                                         # Defining the function to be called when home is accessed
    return render_template('home.html')             # Rendering the home.html file

@app.route('/predict',methods=['POST'])
def predict():
    age = int(request.form["age"])
    sex = int(request.form["sex"])
    bmi = float(request.form["bmi"])
    children = int(request.form["children"])
    smoker = int(request.form["smoker"])
    region = int(request.form["region"])

    input_data = (age, sex, bmi, children, smoker, region)
    input_array = np.asarray(input_data).reshape(1,-1)
    prediction = model.predict(input_array)

    return render_template('home.html',prediction_text = f'Your insurance cost is ${prediction[0]}')


if __name__ == "__main__":                         # Defining the main function
    app.run(debug = True)                          # Running the app in debug mode