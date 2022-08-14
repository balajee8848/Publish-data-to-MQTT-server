from configFileOps import *
from sensorData import *
from convertToJson import *

import time
import paho.mqtt.client as mqtt

def main():
    #Checking for config file
    configFile.isPresent()

    #Creating a instance
    client = mqtt.Client()

    #fetching broker and portID from config file
    broker = str(configFile.getProp("broker", "link"))
    portID = int(configFile.getProp("broker", "portID"))

    #Connecting to the broker
    try:
        client.connect(broker, portID)
    except Exception as e:
        print("Not able to connect to broker")
        exit()

    print("Connected with broker")

    #publishing time and temperature data continuously
    while True:
        #fetching data from sensor
        dataFromSensor = sensorData.fetch()

        #generating payload
        payload = convertToJson.get(dataFromSensor)
    
        #publishing the data
        client.publish("Temperature Data/", payload)
        print(payload)
        
        #waiting for a second
        time.sleep(1)

    #unreachale code
    client.disconnect()

if __name__ == "__main__":
    main()
