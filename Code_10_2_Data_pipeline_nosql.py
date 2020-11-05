##Python Script to Implement the Pipeline

#Define the API KEY ( this can be found in the data.gov.in account section for registered users)

API_KEY = <YOUR API KEY>

#Import the requests library
import requests

#Construct the GET REQUEST

response = requests.get(
             'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070',
             params=[('api-key',API_KEY ),
                    ('format','json'),
                    ('offset',0),
                    ('limit',20)],
             )

#Check if the request was successful - a scuccess request returns a status code 200

if response.status_code == 200:
    print('Success!')
else:
    print('Some Error Occured')
    
#If the you see a success message then you can extract the values from the JSON response
json_response = response.json()

#Import the MongoClient from PyMongo Library
from pymongo import MongoClient

#Define the connection string to your MongoDB instance
# You remember we did not set-up any password while installing MongoDB

client = MongoClient('mongodb://localhost:27017')

#Access the Database
db = client['data-gov-in']

#Access the Collection
posts = db.commodity_prices

#Insert the fist commodity price data into database
result = posts.insert_one(json_response)
