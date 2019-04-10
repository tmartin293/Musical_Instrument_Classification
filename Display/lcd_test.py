import math
import time
import Adafruit_CharLCD as Disp

# setup the different pins the correspond to the GPIO inputs
disp_rs = 'P8_8'
disp_en = 'P8_10'
disp_d4 = 'P8_12'
disp_d5 = 'P8_14'
disp_d6 = 'P8_16'
disp_d7 = 'P8_18'
disp_illuminate = 'P8_7'

# set the border
disp_cols = 16
disp_rows = 2

# Initialize the CharLCD Framework
LCD = Disp.Adafruit_CharLCD(disp_rs, disp_en, disp_d4, disp_d5, disp_d6, disp_d7, disp_cols, disp_rows, disp_illuminate)

# Set the strings to be printed
string1 = "This is a test.\n"
string2 = "Another test 123\n"

# Print the strings
LCD.message(string1 + string2)

# Wait for five seconds
time.sleep(5.0)

# Clear the LCD of all characters
LCD.clear()
