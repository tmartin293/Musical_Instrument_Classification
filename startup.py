"""
Based on the tutorial from Adafruit: 
https://github.com/adafruit/Adafruit_Python_CharLCD/blob/master/examples/char_lcd.py
"""
import Adafruit_CharLCD as LCD
import Adafruit_BBIO.GPIO as GPIO
from scipy.io.wavfile import read
from scipy.fftpack import dct, idct
from numpy import empty_like
import numpy as np
import pyaudio
import datetime
import pickle
import math
import wave
import sys
import time

"""
LCD configuration
"""
lcd_rs        = 'P8_8'
lcd_en        = 'P8_10'
lcd_d4        = 'P8_18'
lcd_d5        = 'P8_16'
lcd_d6        = 'P8_14'
lcd_d7        = 'P8_12'
lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

def toggle_cursor(state):
    lcd_clear()
    # state is a Boolean, example state = True to turn it on
    lcd.show_cursor(state)

# Max String
max_disp    =   "1234567890123456\n1234567890123456"
"""
LCD Error Strings
"""
# Audio Streaming
mic_err     =   "Failed to\nConnect to Mic\n"
record_err  =   "Failed to\nSave Audio\n"
len_err     =   "Recording Length\nExceeded\n"
# Preprocessing
mfcc_err    =   "Failed to\nPreprocess Audio\n"
# ML
predict_err =   "Failed to Guess\nInstrument\n"
"""
LCD Instrument Strings
"""
# Correct Output
results     =   "Instrument =\n"
instruments = [ "Cello\n", "Clarinet\n", "Flute\n",
                "Guitar\n", "Saxophone\n", "Trumpet\n",
                "Violin\n"]
def lcd_print(msg):
    lcd.message(msg)

def lcd_clear():
    lcd.clear()

def print_inst(num):
    if(num < len(instruments) and num > len(instruments)):
        lcd_print("Wrong Instrument\nDetected\n")
    else:
        lcd_print(results + instruments[num])

"""
Button Configuration
"""
button = "P8_8"

def SetupButton():
    GPIO.setup(button,GPIO.IN)
    GPIO.add_event_detect(button,GPIO.RISING)

def CleanAll():
    GPIO.cleanup()

def EventDetected():
    if(GPIO.event_detected(button)):
        return True
    return False
	
"""
This should be were we include all the parts of the software
I am going to wait until Friday to finish this
"""


def main():
    timeout = 100
    counter = 0
    lcd_print("Press Button\nTo Record\n")
    while(counter < timeout):
        time.sleep(0.1)
        if(EventDetected()):
            print("Button pressed!")
        counter = counter + 1
    CleanAll()
        

main()
