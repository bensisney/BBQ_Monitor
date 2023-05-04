import drivers.thermocouples as tc
import drivers.localSensor as local
import drivers.lcdRgbBacklight as lcdRGB
import drivers.lcdText as lcdText
import drivers.mqttLocal as mqttLocal
import drivers.mqttCloud as mqttCloud
from datetime import datetime
from time import sleep

# Global Variable Init
DEBUG_PRINT = False
pitAdcChannel = 1
foodAdcChannel = 2
pitTemp = 0
foodTemp = 0
localTemp = 0
localHumidity = 0

def readThermocouples():
   if DEBUG_PRINT: (f'{datetime.now().strftime(timeFormat)} - Reading TCs')
   global pitTemp
   pitTemp = tc.getThermocoupleTemp(pitAdcChannel,'F')
   global foodTemp
   foodTemp = tc.getThermocoupleTemp(foodAdcChannel,'F')

def readDHT():
    if DEBUG_PRINT: print(f'{datetime.now().strftime(timeFormat)} - Reading DHT')
    global localTemp
    localTemp = local.getTemperature('F')
    global localHumidity
    localHumidity = local.getHumidity()

def publishMQTT():
    if DEBUG_PRINT: print(f'{datetime.now().strftime(timeFormat)} - Publishing to MQTT')
    mqttLocal.publishTemps(pitTemp,foodTemp,localTemp,localHumidity)
    mqttCloud.publishTemps(pitTemp,foodTemp,localTemp,localHumidity)

def logData():
    if DEBUG_PRINT: print(f'{datetime.now().strftime(timeFormat)} - Logging Data')
    # Do something HEre

def updateDisplay():
    if DEBUG_PRINT: print(f'{datetime.now().strftime(timeFormat)} - Updating Display')
    screenLine1 = f"PIT TEMP   : {pitTemp:.2f} F\n"
    screenLine2 = f"FOOD TEMP  : {foodTemp:.2f} F\n"
    screenLine3 = f"LOCAL TEMP : {localTemp:.2f} F\n"
    screenLine4 = f"LOCAL HUM  : {localHumidity:.2f} %"
    screenText = screenLine1 + screenLine2 + screenLine3 + screenLine4
    lcdText.update(screenText)

def init():
    lcdText.clear()
    lcdRGB.setColor("White")
    lcdText.update("Initializing")
    readThermocouples()
    readDHT()

# Main Program 
try:
    init()
    lcdRGB.setColor("green",50)
    while True:
        readThermocouples()
        readDHT()
        updateDisplay()
        publishMQTT()
        logData()
        sleep(60)
except KeyboardInterrupt:
    print('Stopping Program')