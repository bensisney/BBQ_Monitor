import board
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Set some constants
LCD_COLUMNS = 20
LCD_ROWS = 4

# Initialise I2C bus.
i2c = board.I2C()

# Initialise the lcd class
lcd = character_lcd.Character_LCD_I2C(i2c, LCD_COLUMNS, LCD_ROWS)

# Initalize Functions
def clear():
    """
    Clears the LCD screen
    """
    lcd.clear()

def update(message):
    """
    Updates the LCD screen with the provided message
    """
    lcd.message = message

# Clear The Screen
lcd.clear()