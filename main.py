from configFileOps import *
from sensorData import *

import time
from datetime import datetime
import random
import json
import paho.mqtt.client as mqtt

#callback
def on_connect(client, userdata, flags, rc):
    print("Connected with broker")

def main():
    #Creating a instance
    client = mqtt.Client()
    client.on_connect = on_connect

    #fetching broker and portID from config file
    broker = str(configFile.getProp("broker","link"))
    portID = int(configFile.getProp("broker","portID"))

    #Connecting to the broker
    client.connect(broker,portID)

    #publishing time and temperature data continuously
    while True:
        #fetching data from sensor
        dataFromSensor = sensorData.fetch()

        #creating the payload
        payload = '{"time":"' + dataFromSensor['currTime'] + '", "temperature":"' + dataFromSensor['temperature'] +'"}'
        payload = json.loads(str(payload))
        payload = json.dumps(payload, indent=4)
    
        #publishing the data
        client.publish("Test/", payload)
        print(payload)
        
        #waiting for a second
        time.sleep(1)

    #unreachale code
    client.disconnect()

if __name__ == "__main__":
    main()
