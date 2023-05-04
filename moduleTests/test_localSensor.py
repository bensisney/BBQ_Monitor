import sys
  
# append the path of the parent directory
sys.path.append("..")

import modules.localSensor as local

print(f"{local.getTemperature()} (°C)")
print(f"{local.getTemperature('F')} (°F)")
print(f"{local.getHumidity()} (%RH)")

# Expected output
# 26.9 (°C) 
# 80.4 (°F)
# 25.3 (%RH)