import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import pathlib
import configparser

# read config file
configPath = pathlib.Path(__file__).parents[1] / "config.cfg"
config = configparser.ConfigParser()
config.read(configPath)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channels 0-3
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

def voltsToTempC(voltage):
    """
    # Convert the ADC voltage reading to °C
    """
    # We are using the AD8495 Thermocouple Amplifier
    # Temperature (°C) = (Vout - 1.25) / 0.005 V
    # Voltage to degrees Celcius
    temperatureC = (voltage-1.25)/0.005 
    return temperatureC

def correctRawThermocoupleTemp(rawTemp,channel):
    """
    Correct raw thermocouple readings by using a two point calibration.
    Expects raw temperatures in °C and compares to a reference in °C
    https://learn.adafruit.com/calibrating-sensors/two-point-calibration
    """
    # TO DO: Pull these in from a config file
    chan0RawLow = config.getfloat('Thermocouple Calibration','chan0RawLow')
    chan0RawHigh = config.getfloat('Thermocouple Calibration','chan0RawHigh')
    chan0RawRange = chan0RawHigh - chan0RawLow
    
    # TO DO: Pull these in from a config file
    chan1RawLow = config.getfloat('Thermocouple Calibration','chan1RawLow')
    chan1RawHigh = config.getfloat('Thermocouple Calibration','chan1RawHigh')
    chan1RawRange = chan1RawHigh - chan1RawLow

    # TO DO: Pull these in from a config file
    chan2RawLow = config.getfloat('Thermocouple Calibration','chan2RawLow')
    chan2RawHigh = config.getfloat('Thermocouple Calibration','chan2RawHigh')
    chan2RawRange = chan2RawHigh - chan2RawLow
    
    # TO DO: Pull these in from a config file
    chan3RawLow = config.getfloat('Thermocouple Calibration','chan3RawLow')
    chan3RawHigh = config.getfloat('Thermocouple Calibration','chan3RawHigh')
    chan3RawRange = chan3RawHigh - chan3RawLow

    referenceLow = config.getfloat('Thermocouple Calibration','referenceLow')
    referenceHigh = config.getfloat('Thermocouple Calibration','referenceHigh')
    referenceRange = referenceHigh - referenceLow
    
    if channel == 0:
        rawLow = chan0RawLow
        rawRange = chan0RawRange
    elif channel == 1:
        rawLow = chan1RawLow
        rawRange = chan1RawRange
    elif channel == 2:
        rawLow = chan2RawLow
        rawRange = chan2RawRange
    elif channel == 3:
        rawLow = chan3RawLow
        rawRange = chan3RawRange
    else:
        # TO DO:
        # Figure out how to add a useful exception
        # For now, use defaults
        rawLow = 0.01
        rawRange = 99.99
    
    correctedTemp = (((rawTemp - rawLow) * referenceRange) / rawRange) + referenceLow
    
    return correctedTemp

def convertCtoF(tempC):
    """
    Convert temperature in celsius  to Temperature in fahrenheit
    """
    tempF = (tempC * 9/5) +  32
    return tempF

def getVoltage(channel):
    """
    Gets the voltage from the specified channel of the ADC
    """
    if channel == 0:
        voltage = chan0.voltage
    elif channel == 1:
        voltage = chan1.voltage
    elif channel == 2:
        voltage = chan2.voltage
    elif channel == 3:
        voltage = chan3.voltage
    else:
        # Figure out how to add a useful exception
        # For now, default to chan0
        voltage = chan0.voltage
    return voltage     
    
def getRawThermocoupleTemp(channel, unit = "C"):
    """
    Get the raw (uncorrected) thermocouple temperature
    """
    temp_c = voltsToTempC(getVoltage(channel))

    if unit == "C":
        return temp_c
    elif unit == "F":
        return convertCtoF(temp_c)

def getThermocoupleTemp(channel, unit = "C"):
    """
    Get the corrected thermocouple temperature
    """
    temp_c = correctRawThermocoupleTemp(voltsToTempC(getVoltage(channel)),channel)
    
    if unit == "C":
        return temp_c
    elif unit == "F":
        return convertCtoF(temp_c)
    

