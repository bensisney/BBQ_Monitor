# script to test the 4 channels of the ads1115
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

chan1RawLow = 0.12
chan1RawHigh = 98.24
chan1RawRange = chan1RawHigh - chan1RawLow

chan2RawLow = 1.63
chan2RawHigh = 98.66
chan2RawRange = chan2RawHigh - chan2RawLow

referenceLow = 0.01
referenceHigh = 99 #based on elevation in Austin,Tx
referenceRange = referenceHigh - referenceLow

# Function to convert the voltage reading to °F
def voltsToTemp(voltage):
    # We are using the AD8495 Thermocouple Amplifier
    # Temperature (°C) = (Vout - 1.25) / 0.005 V
    
    # Voltage to degrees Celcius
    temperatureC = (voltage-1.25)/0.005 
    
    return temperatureC
    
def correctTemp(rawTemp,rawLow,rawRange):
    correctedTemp = (((rawTemp - rawLow) * referenceRange) / rawRange) + referenceLow
    return correctedTemp

def CtoF(tempC):
    tempF = (tempC * 9/5) +  32
    return tempF
    
# Print all 4 Channels Raw Codes, Volts, and Temperature in °C
ch1_tempC = correctTemp(voltsToTemp(chan1.voltage),chan1RawLow,chan1RawRange)
ch1_tempF = CtoF(ch1_tempC)
ch2_tempC = correctTemp(voltsToTemp(chan2.voltage),chan2RawLow,chan2RawRange)
ch2_tempF = CtoF(ch2_tempC)

print("Channel 1: {:>8.2f}(°C) | {:>8.2f}(°F)".format(ch1_tempC,ch1_tempF))
print("Channel 2: {:>8.2f}(°C) | {:>8.2f}(°F)".format(ch2_tempC,ch2_tempF))