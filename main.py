from configFileOps import *
from sensorData import *
from convertToJson import *
from setupLog import *

import time
import paho.mqtt.client as mqtt
import logging

def main():
    #Checking for config file
    confFileObj = configFile.isPresent()

    # setup log
    tempLevel = str(configFile.getProp(confFileObj, "logger", "level"))
    setupLog.basicConfiguration(tempLevel)

    #Creating a instance
    client = mqtt.Client()

    #fetching broker and portID from config file
    broker = str(configFile.getProp(confFileObj, "broker", "link"))
    portID = int(configFile.getProp(confFileObj, "broker", "portID"))

    #Connecting to the broker
    try:
        client.connect(broker, portID)
    except Exception as e:
        logging.error('Not able to connect to broker with ' + str(broker) + ' on port ' + str(portID))
        exit()

    logging.info('Connected with broker through ' + str(broker) + ' in port ' + str(portID))

    #publishing time and temperature data continuously
    while True:
        #fetching data from sensor
        dataFromSensor = sensor_Data.fetch()

        #generating payload
        payload = convertToJson.get(dataFromSensor)

        # publishing the data
        flag = client.publish("Temperature Data/", payload)

        if flag[0] == 0:
            logging.info('Pubished data - ' + payload)
        else:
            logging.critical('Client Disconnected - Not able to publish data to broker')
            exit()
        
        #waiting for a second
        time.sleep(1)

    #unreachale code
    client.disconnect()

if __name__ == "__main__":
    main()
