# BBQ_Monitor
Python Code to monitor my BBQ Smoker. This project leverages Adafruit Hardware and Software. It's assembeld with a custom PCB.

- To get the pit and meat temperatures, the Raspberry Pi Zero W reads from a 4 channel ADC, each of those channels can be connected to a thermocouple amplifier.
- To get the local environmental conditions, the pi reads from a combination temperature and humidity sensor mounted to the PCB with the Raspberry Pi Zero W.
- The data is published via MQTT to both a local dashboard (Home Assistant) and a cloud Dashboard (ThingSpeak) for web/phone viewing.
- The data is diplayed locally to the pi on a LCD character display with a RGB backlight for status alerts.
- The data is saved to a *.csv file on the pi itself.

## Hardware Overview
- RaspberryPi Zero W
- DHT22 (Temperature and Humidity Sensor)
- ADS1115 (4 Channel ADC)
- AD8495 (Thermocouple Amplifier)
- 20x4 Character LCD
- Custom PCB
- Various Connectors / Passive devices.

## Software Setup

### Adafruit Circuit Python
This is the current core set of libraries used to work with the various sensors in this project.
https://github.com/adafruit/circuitpython
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
```
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```
### DHT22
https://github.com/adafruit/Adafruit_CircuitPython_DHT
```
sudo pip3 install adafruit-circuitpython-dht
```
### ADS1115 + AD8495
https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15
```
sudo pip3 install adafruit-circuitpython-ads1x15
```
### LCD
https://github.com/adafruit/Adafruit_CircuitPython_CharLCD
```
sudo pip3 install adafruit-circuitpython-charlcd
```
## Misc Notes / Links
- https://learn.adafruit.com/calibrating-sensors/two-point-calibration

## Issues / FAQ
### libgpiod Error
> RuntimeError: Timed out waiting for PulseIn message. Make sure libgpiod is installed.

- Make sure you followed the setup instructions for the Adafruit Circuit Python.
- Try installing libgpiod:
```
sudo apt install libgpiod2
```
### i2c permission denied
> Error: Could not open file `/dev/i2c-1': Permission denied
- Try updating your RaspberryPi Firmware
```
sudo rpi-update
```
- Try chaning user missions on the i2c file
```
sudo chmod a+rw /dev/i2c-*
```
