import requests
import json

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # assuming the response is in JSON format
    else:
        response.raise_for_status()