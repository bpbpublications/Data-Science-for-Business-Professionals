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
