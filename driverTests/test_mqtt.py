import sys
from time import sleep

# append the path of the parent directory
sys.path.append("..")

import drivers.mqtt as mqtt

mqttTopic = 'test/testMessage'

# Main Program
try:
    mqtt.init()
    messageCount = 0
    while 1:
        testMessage = '{}: {}'.format("Hello MQTT World", messageCount)
        print('Sending Message "{}"'.format(testMessage)) 
        mqtt.publish(mqttTopic,messageCount)
        messageCount = messageCount + 1
        sleep(10)
except KeyboardInterrupt:
    print()
    print("\nStopping Program")
    mqtt.stop()