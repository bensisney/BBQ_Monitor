# Imports
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# MQTT 
mqttBroker = '0.0.0.0'
mqttPort = 0
mqttTopic = 'test/testMessage'
mqttUser = 'test'
mqttPass = 'test'
mqttDelay = 5

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# Main Program
try:
    client = mqtt.Client("ha-client")
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(mqttUser,mqttPass)
    client.connect(mqttBroker, mqttPort)
    client.loop_start()
    # give the MQTT client time to start
    time.sleep(2)
    
    messageCount = 0

    while 1:
        testMessage = '{}: {}'.format("Hello MQTT World", messageCount)
        print('Sending Message "{}"'.format(testMessage)) 
        client.publish(mqttTopic,testMessage)
        messageCount = messageCount + 1
        time.sleep(10)
except KeyboardInterrupt:
    print()
    print("\nStopping Program")
    client.loop_stop()