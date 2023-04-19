"""
Simple test for the 20x4 character lcd RGB Backlight
RGB colors are each controlled via PWM.
100% Duty cycle equates off.
0% duty cycle equates on.
"""
import RPi.GPIO as GPIO
from time import sleep

# Set some contants
SLEEP_TIME = 1
SWEEP_DELAY = 0.01
COLOR_SWEEPS = 3
DUTY_CYCLE_START = 100
DUTY_CYCLE_STOP = -1
DUTY_CYCLE_STEP = -1

# Make list of Duty Cycles
dutyCycles = list(range(DUTY_CYCLE_START,DUTY_CYCLE_STOP,DUTY_CYCLE_STEP))

# Pin Numbers are BCM numbered, not Board Numbered
RED_PIN = 4
GREEN_PIN = 22
BLUE_PIN = 27

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

# Start PWM at 100% Duty Cycle (Colors Off)
red_pwm.start(100)
blue_pwm.start(100)
green_pwm.start(100)
sleep(SLEEP_TIME)

# Test Red
red_pwm.start(0)
blue_pwm.start(100)
green_pwm.start(100)
sleep(SLEEP_TIME)

# Test Green
red_pwm.start(100)
blue_pwm.start(100)
green_pwm.start(0)
sleep(SLEEP_TIME)

# Test Blue
red_pwm.start(100)
blue_pwm.start(0)
green_pwm.start(100)
sleep(SLEEP_TIME)

# Test Yellow
red_pwm.start(0)
blue_pwm.start(100)
green_pwm.start(0)
sleep(SLEEP_TIME)

# Test Magenta
red_pwm.start(0)
blue_pwm.start(0)
green_pwm.start(100)
sleep(SLEEP_TIME)

# Test Cyan
red_pwm.start(100)
blue_pwm.start(0)
green_pwm.start(0)
sleep(SLEEP_TIME)

# Test White
red_pwm.start(0)
blue_pwm.start(0)
green_pwm.start(0)
sleep(SLEEP_TIME)

# Do Color Fades

# All Colors Off, Start by sweeping Green up
red_pwm.start(100)
blue_pwm.start(100)
green_pwm.start(100)
for dutyCycle in dutyCycles:
    green_pwm.start(dutyCycle)
    sleep(SWEEP_DELAY)

# Do the full sweep a few times
for x in range(COLOR_SWEEPS):
    # Blue is Off, Sweep Red Up and Sweep Green Down
    for dutyCycle in dutyCycles:
        red_pwm.start(dutyCycle)   
        green_pwm.start(DUTY_CYCLE_START-dutyCycle)
        sleep(SWEEP_DELAY)

    # Green is Off, Sweep Blue Up and Sweep Red Down
    for dutyCycle in dutyCycles:
        blue_pwm.start(dutyCycle)   
        red_pwm.start(DUTY_CYCLE_START-dutyCycle)
        sleep(SWEEP_DELAY)

    # Red is Off, Sweep Green Up and Sweep Blue Down
    for dutyCycle in dutyCycles:
        green_pwm.start(dutyCycle)   
        blue_pwm.start(DUTY_CYCLE_START-dutyCycle)
        sleep(SWEEP_DELAY)

# Red and Blue are Off, Sweep Green Down to fade out
for dutyCycle in dutyCycles:
    green_pwm.start(DUTY_CYCLE_START-dutyCycle)
    sleep(SWEEP_DELAY)

# Finish PWM at 100% Duty Cycle (Colors Off)
red_pwm.start(100)
blue_pwm.start(100)
green_pwm.start(100)

GPIO.cleanup()