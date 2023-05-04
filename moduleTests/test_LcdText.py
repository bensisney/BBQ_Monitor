import sys
  
# append the path of the parent directory
sys.path.append("..")

from time import sleep
import modules.lcdText as lcdText

TEST_MESSAGE = "LCD TEST\n4 Lines\n20 Characters\n12345678901234567890"
SLEEP_TIME = 5

# Test Message
lcdText.clear()
lcdText.update(TEST_MESSAGE)
sleep(SLEEP_TIME)

# Clear The Screen
lcdText.clear()

# Expected output on screen for 5 seconds
#
# LCD TEST
# 4 Lines
# 20 Characters
# 12345678901234567890