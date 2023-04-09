# BBQ_Monitor
Python Code to monitor my BBQ Smoker and Publish via MQTT. Leverages Adafruit Hardware and Software.

Note about i2c enabled on boot

## DHT22
https://github.com/adafruit/Adafruit_CircuitPython_DHT
'sudo pip3 install adafruit-circuitpython-dht'

Note, I found I also needed to install libgpiod2
'sudo apt install libgpiod2'

## ADS1115 + AD8495
https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15
'sudo pip3 install adafruit-circuitpython-ads1x15'

## LCD

https://github.com/adafruit/Adafruit_CircuitPython_CharLCD
'sudo pip3 install adafruit-circuitpython-charlcd'
