#Load the Libraries
from flask import Flask,request,render_template
import pickle
import pandas as pd

#Start a flask app
app = Flask(__name__,template_folder="templates")

# Load the model
regressor = pickle.load(open( "linear_reg_salary_model.p", "rb" ))

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        #Retrieve the value of 'YearsofExperince' from the request body
        data =  request.form.get('YearsExperience')
        df = pd.DataFrame([str(data)], columns=['content'])
        print(data)
        predict_new = regressor.predict(df)
        return render_template('index.html', salary=predict_new.tolist()[0])
    return render_template('index.html', salary = '')
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)
