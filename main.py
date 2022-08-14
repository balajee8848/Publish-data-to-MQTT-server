import time
from datetime import datetime
import random
import paho.mqtt.client as mqtt

#callback
def on_connect(client, userdata, flags, rc):
    print("Connected with broker")

#Creating a instance
client = mqtt.Client()
client.on_connect = on_connect

#Connecting to the broker
client.connect("localhost",1883)

#publishing time and temperature data continuously
while True:
    #fetching the current time
    currTime = datetime.now().strftime("%H:%M:%S")
    
    #updating temperature value as random numbers between 32 and 37
    temp = str(random.randrange(32,37)) + " C"
    
    json = {"time":str(currTime), "temp":str(temp)}
    
    #publishing the data
    client.publish("Test/", str(json))
    
    #waiting for a second
    time.sleep(1)

#unreachale code
client.disconnect()

