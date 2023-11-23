import codecs
# -*- coding: UTF-8 -*-

import paho.mqtt.client as mqtt
import json
import time

#from django.template.defaultfilters import random

#import random



if __name__ == '__main__':  
    while True:
        client = mqtt.Client()
        client.on_connect
        client.username_pw_set('infilink','3whDyeH9')
        client.connect('mqtt-device.fetiot3s1.fetnet.net', 8884, 60)
        #power_t = random.randint(1,10)
        
        payload_iaq = {"test":1000} #json
        print(client.publish("v1/devices/me/attributes", json.dumps(payload_iaq)))
        time.sleep(10)
    