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

#Define a empty list where the extracted data will be cached before being written to dataframe
import pandas as pd
arrival_date = []
commodity = []
district = []
market = []
max_price = []
min_price = []
modal_price = []
state = []
timestamp = []
variety = []

#Extract the data from json response
records = json_response["records"]
print("The records in records fiels are of type ",type(records))

# Run a loop over list to extract sub-list data
for item in records:
    arrival_date.append(item["arrival_date"])
    commodity.append(item["commodity"])
    district.append(item["district"])
    market.append(item["market"])
    max_price.append(item["max_price"])
    min_price.append(item["min_price"])
    modal_price.append(item["modal_price"])
    state.append(item["state"])
    timestamp.append(item["timestamp"])
    variety.append(item["variety"])

#All the data extracte via API is now stored in list. let's combine all lists into one single dataframe

df = pd.DataFrame({ 'timestamp':timestamp,
                    'state':state,
                    'district':district,
                    'market':market,
                    'commodity':commodity,
                    'variety':variety,
                    'arrival_date':arrival_date,
                    'min_price':min_price,                 
                    'max_price':max_price,
                    'modal_price':modal_price,
                  })

##Once the data-frame df is ready - we open a database connection and write the dataframe into database
from sqlalchemy import create_engine
db_string = "postgresql://postgres:postgres@localhost:5432/data-gov-in"

db = create_engine(db_string)

#Write data to data table
df.to_sql('commodity_prices', con=db, if_exists='replace')

#Retrieve data to see if got written properly
result_set = db.execute("SELECT * FROM public.commodity_prices")  
for r in result_set:  
    print(r)