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

# Function to convert the voltage reading to °F
def voltsToTemp(voltage):
    # We are using the AD8495 Thermocouple Amplifier
    # Temperature (°C) = (Vout - 1.25) / 0.005 V
    
    # Voltage to degrees Celcius
    temperatureC = (voltage-1.25)/0.005 
    
    # Celcius to Fahrenheit
    #temperatureF = (temperatureC * 9/5) +  32
    
    return temperatureC

# Print all 4 Channels Raw Codes, Volts, and Temperature in °C
print("Channel 0: {:>6}(codes) | {:>6.3f}(V) | {:>8.2f}(°C)".format(chan0.value, chan0.voltage, voltsToTemp(chan0.voltage)))
print("Channel 1: {:>6}(codes) | {:>6.3f}(V) | {:>8.2f}(°C)".format(chan1.value, chan1.voltage, voltsToTemp(chan1.voltage)))
print("Channel 2: {:>6}(codes) | {:>6.3f}(V) | {:>8.2f}(°C)".format(chan2.value, chan2.voltage, voltsToTemp(chan2.voltage)))
print("Channel 3: {:>6}(codes) | {:>6.3f}(V) | {:>8.2f}(°C)".format(chan3.value, chan3.voltage, voltsToTemp(chan3.voltage)))

