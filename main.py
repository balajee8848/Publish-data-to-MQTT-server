import json

from configFileOps import *
from sensorData import *
from convertToJson import *
from setupLog import *

import time
import paho.mqtt.client as mqtt
import logging

####GLOBAL DECLARATIONS####
#sleep time
sleepTime = 5
#min and max values
min = 30
max = 40

#callback function
def on_message(client, userdata, msg):
    global sleepTime
    global min
    global max
    recvdStr = msg.payload.decode()
    #converting string to dictionary
    temp = json.loads(recvdStr)
    #assigning values to global variables according to the values given
    if temp["type"] == "interval":
        sleepTime = temp["value"]
    elif temp["type"] == "config":
        min = temp["random_min"]
        max = temp["random_max"]

def main():
    global sleepTime
    global min
    global max
    #Checking for config file
    confFileObj = configFile.isPresent()

    # setup log
    tempLevel = str(configFile.getProp(confFileObj, "logger", "level"))
    setupLog.basicConfiguration(tempLevel)

    #Creating a instance
    client = mqtt.Client()
    client.on_message = on_message

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

    #subscribing to a particular topic
    client.subscribe('/config/config')

    #publishing time and temperature data continuously
    while True:
        client.loop_start()
        #fetching data from sensor
        dataFromSensor = sensor_Data.fetch(min,max)

        #generating payload
        payload = convertToJson.get(dataFromSensor)

        # publishing the data
        flag = client.publish("Temperature Data/", payload)

        if flag[0] == 0:
            logging.info('Pubished data - ' + payload)
        else:
            logging.critical('Client Disconnected - Not able to publish data to broker')
            logging.critical('Trying to reconnect...')
            connectionMadeFlag = 1
            while connectionMadeFlag != 0:
                try:
                    connectionMadeFlag = client.connect(broker,portID)
                    if connectionMadeFlag == 0:
                        logging.info('Reconnected with broker through ' + str(broker) + ' in port ' + str(portID))
                except Exception as err:
                    pass
        
        #waiting for a second
        time.sleep(sleepTime-1)
        client.loop()

    #unreachale code
    client.disconnect()

if __name__ == "__main__":
    main()
