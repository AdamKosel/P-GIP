
# import urllib library
from urllib.request import urlopen

# import json
import json

# store the URL in url as parameter for urlopen

key = X  # replace X with api key from ipgolocation.com
prompt = "Enter an IP: "
IP = input(prompt)

url = 'https://api.ipgeolocation.io/ipgeo?apiKey=' + key + '&ip=' + IP

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
print(data_json)


#format data
