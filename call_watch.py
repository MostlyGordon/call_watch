#!/usr/local/bin/python
import socketio
import json
from pync import Notifier

# Program to monitor Brandmeister TG91 and notify when a call is made from a specific call sign
# By: Gordon VK3TEN 2023-08-01

# Callsigns to monitor
calls = ['KC7ZOH', "VK3XEM", "VK3UT", "VK3YHT", "VK3TEN"]

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

@sio.on("mqtt")
def on_message(data):
    responce = json.loads(data['payload'])
    source_call = responce['SourceCall']
    source_name = responce['SourceName']
    source_id = responce['SourceID']
    destination_id = responce['DestinationID']
    if destination_id == 91:
        print(f"{source_id} - {source_call} - {source_name} - {destination_id}")
        if source_call in calls:
            Notifier.notify(f"{source_call} is on Brandmeister TG91")
    return

sio.connect(url='https://api.brandmeister.network', socketio_path="/lh/socket.io", transports="websocket")
sio.wait()