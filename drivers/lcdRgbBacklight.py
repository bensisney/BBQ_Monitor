"""
TO DO
"""
import RPi.GPIO as GPIO

# Pin Numbers are BCM numbered, not Board Numbered
RED_PIN = 4
BLUE_PIN = 27
GREEN_PIN = 22

# Setup GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN,GPIO.OUT)
GPIO.setup(BLUE_PIN,GPIO.OUT)
GPIO.setup(GREEN_PIN,GPIO.OUT)

# Create PWM instances
red_pwm = GPIO.PWM(RED_PIN,100)
blue_pwm = GPIO.PWM(BLUE_PIN,100)
green_pwm = GPIO.PWM(GREEN_PIN,100)

# Define some preset colors, data is stored in RGB order.
BACKLIGHT_COLORS = {'red':      [100, 0, 0],
                    'blue':     [0, 0, 100],
                    'green':    [0, 100, 0],
                    'yellow':   [100, 75, 0],
                    'magenta':  [100, 0, 100],
                    'cyan':     [0, 100, 100],
                    'purple':   [25, 0, 75],
                    'orange':   [75, 15, 0],
                    'white':    [100, 100, 100]}

def percentToDuty(percent):
    """
    TO DO
    """
    dutyCycle = 100 - percent
    return dutyCycle

def setColor(color, brightness = 100):
    """
    TO DO
    """
    # TO DO: Add error handling for if color isn't defined
    
    # Get color from dictionary
    rgbValues = BACKLIGHT_COLORS[color.lower()]
    
    # Set Colors
    red_pwm.start(percentToDuty(rgbValues[0] * brightness/100))
    green_pwm.start(percentToDuty(rgbValues[1] * brightness/100))
    blue_pwm.start(percentToDuty(rgbValues[2] * brightness/100))

def setRGB(percent_red, percent_green, percent_blue):
    """
    TO DO
    """
    red_pwm.start(percentToDuty(percent_red))
    green_pwm.start(percentToDuty(percent_green))
    blue_pwm.start(percentToDuty(percent_blue))

def turnOff():
    """
    TO DO
    """
    red_pwm.start(100)
    green_pwm.start(100)
    blue_pwm.start(100)

def cleanup():
    """
    TO DO
    """
    GPIO.cleanup()