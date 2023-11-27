'''
import codecs
# -*- coding: UTF-8 -*-

import paho.mqtt.client as mqtt
import json
import time
import ssl

#from django.template.defaultfilters import random

#import random



if __name__ == '__main__':  
    while True:
        
        print ("Production")
        client = mqtt.Client()
        client.on_connect
        client.username_pw_set('3whDyeH9','infilink')
        client.connect('mqtt-device.fetiot3p1.fetnet.net', 8884, 60)
        #power_t = random.randint(1,10)
        
        payload_iaq = {"test":1000} #json
        print(client.publish("/smartbuilding/v1/telemetry/nh220", json.dumps(payload_iaq)))
        time.sleep(10)
        
        print ("Station")
        #client = mqtt.Client('', True, None, mqtt.MQTTv31)
        #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client = mqtt.Client()
        #client.on_connect
        client.username_pw_set('fQdc44pz','infilink')
        client.connect('mqtt-device.fetiot3s1.fetnet.net', 8884, 60)
        #power_t = random.randint(1,10)
        
        payload_iaq = [{"access_token": "8G60nMefNfBUeoY7ebm6",
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":{"F4EL1_BackupPower":100}}]}]
        print(client.publish("/smartbuilding/v1/telemetry/nh220", json.dumps(payload_iaq)))
        time.sleep(30)

        
'''
import paho.mqtt.client as mqtt
import json

HOST = "mqtt-device.fetiot3p1.fetnet.net"
PORT = 8884
USER = '3whDyeH9'
PASS = 'infilink'
TOPIC = "/smartbuilding/v1/telemetry/nh220"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    # msg.topic
    messages = json.loads(msg.payload)
    print(messages)
    print("test")

if __name__ == '__main__':

    client = mqtt.Client()
    client.username_pw_set(USER, PASS)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()