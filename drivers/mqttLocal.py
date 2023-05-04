# Imports
from time import sleep
import paho.mqtt.client as mqttClient
import paho.mqtt.publish as mqttPublish
import pathlib
import configparser

# read config file
configPath = pathlib.Path(__file__).parents[1] / "config.cfg"
config = configparser.ConfigParser()
config.read(configPath)

# Get MQTT Settings from config file
mqttBroker = config.get('MQTT Local','broker')
mqttPort = config.getint('MQTT Local','port')
mqttUser = config.get('MQTT Local','username')
mqttPass = config.get('MQTT Local','password')
pitTempTopic = config.get('MQTT Local','pitTempTopic')
foodTempTopic = config.get('MQTT Local','foodTempTopic')
localTempTopic = config.get('MQTT Local','localTempTopic')
localHumidityTopic = config.get('MQTT Local','localHumidityTopic')

client = mqttClient.Client("ha-client")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if __debug__: print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def init():
    """
    Initalize our MQTT Connection
    """
    client.on_connect = on_connect
    #client.on_message = on_message
    client.username_pw_set(mqttUser,mqttPass)
    client.connect(mqttBroker, mqttPort)
    client.loop_start()
    # give the MQTT client time to start
    sleep(2)

def publish(topic,message):
    """
    Generic Publish. Can be any message to any topic.
    """
    client.publish(topic,message)

def publishTemps(pitTemp,foodTemp,localTemp,localHumidity):
    """
    This is the main publish we will use as it's built specifically for what we want to send.
    """
    client.publish("bbqmon/pitTemp",pitTemp)
    client.publish(foodTempTopic,foodTemp)
    client.publish(localTempTopic,localTemp)
    client.publish(localHumidityTopic,localHumidity)

def stop():
    client.loop_stop()