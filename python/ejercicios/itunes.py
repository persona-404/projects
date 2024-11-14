import requests
import sys
import json

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=weezer")
#print(json.dumps(response.json(), indent=2))

json_response = response.json()

for result in json_response["results"]:
    print(result["trackName"])
