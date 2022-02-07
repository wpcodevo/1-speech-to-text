from config import *
api_key = api_key

import requests

endpoint = "https://api.assemblyai.com/v2/upload"


headers = {
  "authorization": api_key,
  "content_type": "application/json"
}

def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data


response = requests.post(endpoint, headers=headers, data=read_file('audio.mp3'))
audio_url= response.json()['upload_url']

transcript_request = {'audio_url': audio_url}
request_endpoint = "https://api.assemblyai.com/v2/transcript"
transcript_response = requests.post(request_endpoint, json=transcript_request, headers=headers)

audio_id = transcript_response.json()['id']
status_endpoint = "https://api.assemblyai.com/v2/transcript/" + audio_id
polling_response = requests.get(status_endpoint, headers=headers)

if polling_response.json()['status'] != 'completed':
   print(polling_response.json())
else:
   with open(audio_id + '.txt', 'w') as f:
       f.write(polling_response.json()['text'])
   print('Transcript saved to', audio_id, '.txt')
