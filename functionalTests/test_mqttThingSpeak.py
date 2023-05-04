import paho.mqtt.publish as publish
import time
import random
 
channel_ID = "1234567"

# The hostname of the ThingSpeak MQTT broker.
mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "aBcDeFgHiJkLmNoPqRsTuVw"
mqtt_username  = "aBcDeFgHiJkLmNoPqRsTuVw"
mqtt_password  = "aBcDeFgHiJkLmNoPqRsTuVw"

t_transport = "websockets"
t_port = 80

# Create the topic string.
topic = "channels/" + channel_ID + "/publish"

try:
    count = 0
    while True:
        randomNumber = random.randrange(220,230) 
        payload = "field1=" + str(randomNumber) + "&field2=" + str(count)
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})
        count = count + 1
        time.sleep(60)
except Exception as e:
    print (e)
except KeyboardInterrupt:
    print("Keyboard Interrupt")