#Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datasets
data = pd.read_csv('Salary_Data.csv')

#Have a look at top 5 rows of data
data.head()

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

# Predicting the Test set result ￼

Y_Pred = regressor.predict(X_Test)

# Visualising the Test set results

plt.scatter(X_Test, Y_Test, color = 'red')
plt.plot(X_Train, regressor.predict(X_Train), color = 'blue')
plt.title('Salary vs Experience  (Training Set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

#Load the New Employee Data
new_data = pd.read_csv('new_employee.csv')
new_employee_exp = new_data[['YearsExperience']].values

#Load the model
import pickle
pickle.load(open( "linear_reg_salary_model.p", "rb" ))

#Make the predictions
predict_new = regressor.predict(new_employee_exp)

print(predict_new)

#Store the predictions into a csv file
np.savetxt("New Employee Salary Prediction.csv", predict_new, delimiter=",")