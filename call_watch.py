"""#!/usr/local/bin/python - works on my Mac"""
import socketio
import json
from notifypy import Notify

# Program to monitor Brandmeister and notify when a call is made from a specific call signs
# By: Gordon VK3TEN 2023-08-01

# Callsigns to monitor
calls = ['KC7ZOH', "VK3XEM", "VK3UT", "VK3YHT", "VK3TIM", "DG0TD", "WC3H"]

# Talk Groups to monitor
tg = [91, 31656]

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
    if destination_id in tg:
        #Comment out the next line if you don't want to see all calls on the console
        print(f"{source_id} - {source_call} - {source_name} - {destination_id}")
        if source_call in calls:
            notification = Notify()
            notification.title = "Call Watch"
            notification.message = f"{source_call} - {source_name} is on BrandMeister TG{destination_id}"
            notification.send()
    return

sio.connect(url='https://api.brandmeister.network', socketio_path="/lh/socket.io", transports="websocket")
sio.wait()