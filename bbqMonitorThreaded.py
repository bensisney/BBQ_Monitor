import drivers.thermocouples as tc
import drivers.localSensor as local
import drivers.lcdRgbBacklight as lcdRGB
import drivers.lcdText as lcdText
import drivers.mqttLocal as mqttLocal
import drivers.mqttCloud as mqttCloud
import modules.csvlog as csvlog
from threading import Thread
from datetime import datetime
from time import sleep
import time
import configparser

# read config file
configPath = "config.cfg"
config = configparser.ConfigParser()
config.read(configPath)

# Global Variable Init
pitAdcChannel = 1
foodAdcChannel = 2
pitTemp = 0
foodTemp = 0
localTemp = 0
localHumidity = 0
startTime = 0
timeFormat = "%m/%d/%y %H:%M:%S.%f"

# How often each thread happens in seconds
TC_INTERVAL = config.getfloat('Program Settings','tcInterval')
DHT_INTERVAL = config.getfloat('Program Settings','dhtInterval')
DISPLAY_INTERVAL = config.getfloat('Program Settings','displayInterval')
MQTT_INTERVAL = config.getfloat('Program Settings','mqttInterval')
LOG_INTERVAL = config.getfloat('Program Settings','logInterval')

# Functions
def sleepTime(interval):
    return (interval - ((time.time() - startTime) % interval))

def readThermocouples():
    if __debug__: print(f'{datetime.now().strftime(timeFormat)} - Reading TCs')
    global pitTemp
    pitTemp = tc.getThermocoupleTemp(pitAdcChannel,'F')
    global foodTemp
    foodTemp = tc.getThermocoupleTemp(foodAdcChannel,'F')

def updateThermocouples():
    while True:
        readThermocouples()
        sleep(sleepTime(TC_INTERVAL))

def readDHT():
    if __debug__: print(f'{datetime.now().strftime(timeFormat)} - Reading DHT')
    global localTemp
    localTemp = local.getTemperature('F')
    global localHumidity
    localHumidity = local.getHumidity()

def updateDHT():
    while True:
        readDHT()
        sleep(sleepTime(DHT_INTERVAL))

def publishMQTT():
    while True:
        if __debug__: print(f'{datetime.now().strftime(timeFormat)} - Publishing to MQTT')
        mqttLocal.publishTemps(pitTemp,foodTemp,localTemp,localHumidity)
        mqttCloud.publishTemps(pitTemp,foodTemp,localTemp,localHumidity)
        sleep(sleepTime(MQTT_INTERVAL))

def logData():
    while True:
        if __debug__: print(f'{datetime.now().strftime(timeFormat)} - Logging Data')
        csvlog.updateLog(pitTemp,foodTemp,localTemp,localHumidity)
        sleep(sleepTime(LOG_INTERVAL))

def updateDisplay():
    while True:
        if __debug__: print(f'{datetime.now().strftime(timeFormat)} - Updating Display')
        screenLine1 = f"PIT TEMP   : {pitTemp:.2f} F\n"
        screenLine2 = f"FOOD TEMP  : {foodTemp:.2f} F\n"
        screenLine3 = f"LOCAL TEMP : {localTemp:.2f} F\n"
        screenLine4 = f"LOCAL HUM  : {localHumidity:.2f} %"
        screenText = screenLine1 + screenLine2 + screenLine3 + screenLine4
        lcdText.update(screenText)
        sleep(sleepTime(DISPLAY_INTERVAL))

def init():
    if __debug__: print(f'{datetime.now().strftime(timeFormat)} - Initializing')
    lcdText.clear()
    lcdRGB.setColor("White")
    lcdText.update("\nInitializing")
    mqttLocal.init()
    csvlog.createLog(config.get('Program Settings','csvLogDir'))
    readThermocouples()
    readDHT()
    lcdRGB.setColor("green")

# Main Program 

thread1 = Thread(target = updateThermocouples)
thread2 = Thread(target = updateDHT)
thread3 = Thread(target = updateDisplay)
thread4 = Thread(target = publishMQTT)
thread5 = Thread(target = logData)

try:
    init()
    startTime = time.time()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
except KeyboardInterrupt:
    print('Stopping Program')