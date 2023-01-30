# import paho.mqtt.client as mqtt
# import numpy as np
# # 0. define callbacks - functions that run when events happen.
# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#    print("Connection returned result: "+str(rc))
#   # Subscribing in on_connect() means that if we lose the connection and
#   # reconnect then subscriptions will be renewed.
#   # client.subscribe("ece180d/test")
# # The callback of the client when it disconnects.
# def on_disconnect(client, userdata, rc):
#   if rc != 0:
#     print('Unexpected Disconnect')
#   else:
#     print('Expected Disconnect')
# # The default message callback.
# # (won't be used if only publishing, but can still exist)
# def on_message(client, userdata, message):
#   print('Received message: "' + str(message.payload) + '" on topic "' +
#        message.topic + '" with QoS ' + str(message.qos))
# # 1. create a client instance.
# client = mqtt.Client()
# # add additional client options (security, certifications, etc.)
# # many default options should be good to start off.
# # add callbacks to client.
# client.on_connect = on_connect
# client.on_disconnect = on_disconnect
# client.on_message = on_message
# # 2. connect to a broker using one of the connect*() functions.
# client.connect_async('test.mosquitto.org:8080')
# # 3. call one of the loop*() functions to maintain network traffic flow with the broker.
# client.loop_start()
# # 4. use subscribe() to subscribe to a topic and receive messages.
# # 5. use publish() to publish messages to the broker.
# # payload must be a string, bytearray, int, float or None.
# for i in range(10):
#   client.publish('ece180d/test', float(np.random.random(1)), qos=1)
# # 6. use disconnect() to disconnect from the broker.
# client.loop_stop()
# client.disconnect()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2010-2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# All rights reserved.

# This shows a simple example of an MQTT subscriber using connect_srv method.

import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, rc):
    print("Connected to %s:%s" % (mqttc._host, mqttc._port))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
#mqttc.on_log = on_log
mqttc.connect_srv("mosquitto.org", 60)
mqttc.subscribe("$SYS/broker/version", 0)


rc = 0
while rc == 0:
    rc = mqttc.loop()

print("rc: "+str(rc))