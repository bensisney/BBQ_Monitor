# Imports
from time import sleep
import paho.mqtt.publish as publish
import pathlib
import configparser

# read config file
configPath = pathlib.Path(__file__).parents[1] / "config.cfg"
config = configparser.ConfigParser()
config.read(configPath)

# Get MQTT Settings from config file
mqttBroker = config.get('MQTT Cloud','broker')
mqttPort = config.getint('MQTT Cloud','port')
mqttUser = config.get('MQTT Cloud','username')
mqttPass = config.get('MQTT Cloud','password')
mqttClientId = config.get('MQTT Cloud','clientId')
mqttchannelId = config.get('MQTT Cloud','channelId')

# Create the topic string.
topic = "channels/" + mqttchannelId + "/publish"

def publishTemps(pitTemp,foodTemp,localTemp,localHumidity):
    """
    Builds the payload string and publishes the temps/humidity to ThingSpeak
    """
    field1 = "field1=" + str(pitTemp)
    field2 = "&field2=" + str(foodTemp)
    field3 = "&field3=" + str(localTemp)
    field4 = "&field4=" + str(localHumidity)
    payload= field1 + field2 + field3 + field4
    publish.single(topic, payload, hostname=mqttBroker, transport="websockets", port=mqttPort, client_id=mqttClientId, auth={'username':mqttUser,'password':mqttPass})