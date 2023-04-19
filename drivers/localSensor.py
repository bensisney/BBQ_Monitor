import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=True)

def convertCtoF(tempC):
    """
    Convert temperature in celsius  to Temperature in fahrenheit
    """
    tempF = (tempC * 9/5) +  32
    return tempF

def getTemperature(unit = "C"):
    while True:
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = convertCtoF(temperature_c)
            if unit == "C":
                return temperature_c
            elif unit == "F":
                return temperature_f
        except RuntimeError as error:
            # Errors happen pretty often on the Pi Zero, just keep trying
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
    
def getHumidity():
    while True:
        try:
            humidity = dhtDevice.humidity
            return humidity
        except RuntimeError as error:
            # Errors happen pretty often on the Pi Zero, just keep trying
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error