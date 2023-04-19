import time
import board
import adafruit_dht

# Initial the dht device
dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=True)

while True:
    try:
        # Get Readings
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        
        # Print Readings
        print(f"Temperature: {temperature_f:.2f} F / {temperature_c:.2f} C")
        print(f"Humidity {humidity} %RH")
        
        # If succesful, close sensor and break
        dhtDevice.exit()
        break
    except RuntimeError as error:
        # If error happens, keep trying
        print(f"Error: {error.args[0]}")
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
