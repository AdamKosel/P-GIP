# import urllib library
from urllib.request import urlopen

# import json
import json

# store the URL in url as
# parameter for urlopen
url = 'https://api.ipgeolocation.io/ipgeo?apiKey=7d691d65b7bd41f2a8c8d45713354da4&ip=8.8.8.8'

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
print(data_json)
