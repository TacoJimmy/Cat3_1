
import codecs
# -*- coding: UTF-8 -*-

import paho.mqtt.client as mqtt
import json
import time
import ssl

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
        print ("Production")
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client = mqtt.Client()
        client.tls_set_context(context)
        client.username_pw_set('infilink','fQdc44pz')
        client.connect('mqtt-device.fetiot3s1.fetnet.net', 8884, 60)
        #power_t = random.randint(1,10)
        
        payload_iaq = [{"access_token": "8G60nMefNfBUeoY7ebm6",
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":{"F4EL1_BackupPower":100}}]}]
        print(client.publish("/smartbuilding/v1/telemetry/nh220", json.dumps(payload_iaq)))
        time.sleep(10)

        print ("Station")
        client1 = mqtt.Client('', True, None, mqtt.MQTTv31)
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client1 = mqtt.Client()
        client1.tls_set_context(context)
        client1.username_pw_set('infilink','3whDyeH9')
        client1.connect('mqtt-device.fetiot3p1.fetnet.net', 8884, 60)
        #power_t = random.randint(1,10)
        
        payload_iaq = [{"access_token": "8G60nMefNfBUeoY7ebm6",
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":{"F4EL1_BackupPower":100}}]}]
        print(client.publish("/smartbuilding/v1/telemetry/nh220", json.dumps(payload_iaq)))
        time.sleep(10)