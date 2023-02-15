import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("julieden/ping")
    client.message_callback_add("julieden/ping",on_message_from_ping)
   
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))
 
def on_message_from_ping(client, userdata, message):
    print("Custom callback  - PING: "+message.payload.decode())
    inp = int(message.payload, "utf-8")
    print("Input: " + inp)
    client.publish("julieden/pong",f"{inp + 1}")
    print("Publishing number")


if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client()
    
    client.on_connect = on_connect
   
    #client.on_message = on_message
    client.connect(host="172.20.10.4", port=1883, keepalive=60)
    time.sleep(4)
    """
    client.publish("julieden/pong",f"{inp + 1}")
    print("Publishing number")
    """ 
    client.loop_forever()
      
