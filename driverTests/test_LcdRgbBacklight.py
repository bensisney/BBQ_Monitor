import sys
  
# append the path of the parent directory
sys.path.append("..")

from time import sleep
import drivers.lcdRgbBacklight as lcdRGB

SLEEP_TIME = 1

# Set Color by name
colors = ["red", "blue", "green","yellow", "purple", "orange", "cyan", "magenta", "white"]
for color in colors:
    lcdRGB.setColor(color)
    sleep(SLEEP_TIME)

# Set color by name with brightness 
lcdRGB.setColor("blue",25)
sleep(SLEEP_TIME)

# Set color by RGB percentage
lcdRGB.setRGB(35,15,5)
sleep(SLEEP_TIME)

lcdRGB.turnOff()

lcdRGB.cleanup()