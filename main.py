import requests
from config import *

api_key = api_key

endpoint = "https://api.assemblyai.com/v2/transcript/"

json= {
  "audio_url": ""
}

headers = {
  "authorization": api_key,
  "content_type": "application/json"
}

def read_file(filename):
   with open(filename, 'rb') as file:
       while True:
           data = file.read(5242880)
           if not data:
               break
           yield data

response = requests.post(endpoint, json=json, headers=headers)
audio_url= response.json()["upload_url"]
