# BBQ_Monitor
Python Code to monitor my BBQ Smoker and Publish via MQTT. Leverages Adafruit Hardware and Software. Put together with a custom PCB and 3D printed enclosure.

## Hardware Overview
- RaspberryPi Zero W
- DHT22
- ADS1115
- AD8495
- LCD
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
