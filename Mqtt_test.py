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
        '''
        print ("Production")
        client = mqtt.Client()
        client.on_connect
        client.username_pw_set('3whDyeH9','infilink')
        client.connect('mqtt-device.fetiot3p1.fetnet.net', 8884, 60)
        #power_t = random.randint(1,10)
        
        payload_iaq = {"test":1000} #json
        print(client.publish("/smartbuilding/v1/telemetry/nh220", json.dumps(payload_iaq)))
        time.sleep(10)
        '''
        print ("Station")
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.on_connect
        client.username_pw_set('fQdc44pz','infilink')
        client.connect('mqtt-device.fetiot3s1.fetnet.net', 8884, 60)
        #power_t = random.randint(1,10)
        
        payload_iaq = {"test":1000} #json
        print(client.publish("/smartbuilding/v1/telemetry/nh220", json.dumps(payload_iaq)))
        time.sleep(10)