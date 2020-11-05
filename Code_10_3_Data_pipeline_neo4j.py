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
                    ('limit',1)],
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

df = pd.DataFrame({'arrival_date':arrival_date,
                  'commodity':commodity,
                  'district':district,
                  'market':market,
                  'max_price':max_price,
                  'min_price':min_price,
                  'modal_price':modal_price,
                  'state':state,
                  'timestamp':timestamp,
                  'variety':variety
                  })

#Writing to neo4j graph
from py2neo import Graph
graph = Graph("bolt://neo4j:admin@localhost:7687")


for index, row in df.iterrows():
    graph.run('''
       CREATE (a:commodity {commodity:$commodity,min_price:$min_price,modal_price:$modal_price,max_price:$max_price}), (b:market {state:$state,district:$district,market:$market}), (c:variety {variety:$variety})
       MERGE (a)-[:SELLS_AT]->(b)
       MERGE (b)-[:IS_OF_VARIETY]->(c)
       ''', parameters = {'commodity': row['commodity'], 'min_price': row['min_price'],'modal_price': row['modal_price'], 'max_price': row['max_price'],'state': row['state'], 'district': row['district'],'market': row['market'],'variety': row['variety']})
