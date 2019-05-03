"""
Configuration
"""
# LCD Setup display - 'Loading...'
    # Import Pickle Model
    # Setup Compenents
        # Button
        # LED
        # Mic

"""
Event Loop
"""
# Prompt user to 'Press Button' to record
# On Event Dected
    # Record Audio
    # Change color to Green
# Prompt user to 'Press Button' to stop recording recording
# On Event Detected
    # Stop Recording Audio
    # Change color to Red
# Normalization
    # Trim
    # Onset Detection
# Predictions
# Display results

"""
Teardown
"""
# GPIO Cleanup
# Audio Stream Terminate






import Output # LCD and LED
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
