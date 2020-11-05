#Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datasets
data = pd.read_csv('Salary_Data.csv')

#Load the values on variables in a array
X = data[['YearsExperience']].values
Y = data[['Salary']].values

# Splitting the into the Training set and Test set

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# Fitting Simple Linear Regression to the training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)

#Store the model as a pickle object
import pickle
pickle.dump(regressor,open( "linear_reg_salary_model.p", "wb" ))
#Load the Libraries
from flask import Flask,request,jsonify
import pickle
import json
import pandas as pd

#Start a flask app
app = Flask(__name__)

# Load the model
regressor = pickle.load(open( "linear_reg_salary_model.p", "rb" ))

@app.route('/predict', methods=['POST'])
def predict():
    #Retrieve the value of 'YearsofExperince' from the request body
    data = request.get_json()
    df = pd.DataFrame([float(data['YearsExperience'])], columns=['content'])
    predict_new = regressor.predict(df)
    result = {'predicted_salary': predict_new.tolist()[0]} 
    return json.dumps((result))
    
if __name__ == '__main__':
    app.run(port=3000, debug=True) 
#import the request library which allows us to make Post/Get etc web request
import requests

#Define the address of host where the application is running
url     = 'http://127.0.0.1:3000/predict'
payload = { "YearsExperience" : 3.2 }
res = requests.post(url,json = payload)
