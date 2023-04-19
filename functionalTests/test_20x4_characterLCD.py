"""
Simple test for the 20x4 character lcd connected to an MCP23008 I2C LCD backpack.
Writes a message to all 4 lines of the screen.
"""
import time
import board
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Set some constants
LCD_COLUMNS = 20
LCD_ROWS = 4
TEST_MESSAGE = "LCD TEST\n4 Lines\n20 Characters\n12345678901234567890"
SLEEP_TIME = 3

# Initialise I2C bus.
i2c = board.I2C()

# Initialise the lcd class
lcd = character_lcd.Character_LCD_I2C(i2c, LCD_COLUMNS, LCD_ROWS)

# Clear The Screen
lcd.clear()

# Test Message
lcd.message = TEST_MESSAGE
time.sleep(SLEEP_TIME)

# Clear The Screen
lcd.clear()