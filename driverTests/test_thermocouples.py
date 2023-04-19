import sys
  
# append the path of the parent directory
sys.path.append("..")

import drivers.thermocouples as tc

channels = [0, 1, 2, 3]

print("Channel | Raw Temp (°C) | Corrected Temp (°C)")
for channel in channels:
    temp_raw = tc.getRawThermocoupleTemp(channel)
    temp_corr = tc.getThermocoupleTemp(channel)
    print(f"{channel} {temp_raw:>20.2f} {temp_corr:>20.2f}")
print("")
print("Channel | Raw Temp (°F) | Corrected Temp (°F)")
for channel in channels:
    temp_raw = tc.getRawThermocoupleTemp(channel,'F')
    temp_corr = tc.getThermocoupleTemp(channel,'F')
    print(f"{channel} {temp_raw:>20.2f} {temp_corr:>20.2f}")

# Expected output if ch 1,2 are in use and 0,3 are disconnected
#
# Channel | Raw Temp (°C) | Corrected Temp (°C)
# 0              -134.37              -132.06
# 1                23.03                23.15
# 2                24.01                22.79
# 3              -133.22              -132.21
#
# Channel | Raw Temp (°F) | Corrected Temp (°F)
# 0              -209.06              -206.21
# 1                73.55                73.67
# 2                75.13                73.07
# 3              -208.47              -205.67

