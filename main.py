import time
import paho.mqtt.client as mqtt

#callback
def on_connect(client, userdata, flags, rc):
    print("Connected with broker")

#Creating a instance
client = mqtt.Client()
client.on_connect = on_connect

#Connecting to the broker
client.connect("localhost",1883)

#publishing data continuously
num = 0
while True:
    client.publish("Test/", str(num))
    num+=1
    time.sleep(1)

#unreachale code
client.disconnect()

