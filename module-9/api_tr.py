import requests
import json

#Sends request to PokeAPI
response = requests.get('http://pokeapi.co/api/v2/generation/?limit=9')

#Function to print unformatted JSON data
def jprint(obj):
    text = json.dumps(obj)
    print(text)

#Function to print formatted JSON data
def jprint2(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Checks if the API request was established successfully
if response.status_code == 200:
    print(f"STATUS CODE {response.status_code}: {str.upper(response.reason)}\n")

    #Prints unformatted JSON data
    print("Not Formatted:")
    jprint(response.json())

    #Prints formatted JSON data
    print("\nFormatted:")
    jprint2(response.json())

#Prints error message if the request was unsuccessful
else:
    print(f"STATUS CODE {response.status_code}: {str.upper(response.reason)}")