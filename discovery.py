import os

import requests
import json
from dotenv import load_dotenv

load_dotenv(".env")
DISCOVERY_URL = os.getenv("DISCOVERY_URL")
SERVICE_NAME = os.getenv("SERVICE_NAME")

def register():
    # Send POST request with JSON data
    response = requests.post(f"{DISCOVERY_URL}/register",
                             data=json.dumps({'name': SERVICE_NAME}),
                             headers={'Content-Type': 'application/json'})

    return response.json()['uuid'], response.json()['port']


def unregister(uuid: str):
    # Send POST request with JSON data
    response = requests.post(f"{DISCOVERY_URL}/unregister",
                             data=json.dumps({'uuid': uuid}),
                             headers={'Content-Type': 'application/json'})

    return response.json()