#import the request library which allows us to make Post/Get etc web request
import requests

#Define the address of host where the application is running
url     = 'http://127.0.0.1:3000/predict'
payload = { "YearsExperience" : 3.2 }
res = requests.post(url,json = payload)

print(res.json())
