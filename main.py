import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

#callback
def on_connect(client, userdata, flags, rc):
    print("Connected with broker")

#Creating a instance
client = mqtt.Client()
client.on_connect = on_connect

#Connecting to the broker
client.connect("localhost",1883)

#publishing a data for a single time
publish.single("Test/", "Single message from python")

#dsconnecting
client.disconnect()