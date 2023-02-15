import paho.mqtt.client as mqtt
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("julieden/ping")
    client.message_callback_add("julieden/pong",on_message_from_ping)
   
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_message_from_ping(client, userdata, message):
    print("Custom callback  - PING: "+message.payload.decode())


if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client()
    
    client.on_connect = on_connect
    
    client.connect(host="172.20.10.4", port=10000, keepalive=60)
    
    client.loop_start()
    time.sleep(1)
    
    client.on_message = on_message
    client.connect(host="172.20.10.4", port=10000, keepalive=60)
    time.sleep(4)
    client.publish("julieden/pong",f"{inp}")
    print("Publishing number")
    
    client.loop_forever()
      
