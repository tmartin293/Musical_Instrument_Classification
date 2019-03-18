import math
import time
import Adafruit_CharLCD as Disp

# Configure the BeagleBone Black as follows:
disp_rs = ‘P8_8’
disp_en = ‘P8_10’
disp_d4 = ‘P8_18’
disp_d5 = ‘P8_16’
disp_d6 = ‘P8_14’
disp_d7 = ‘P8_12’
disp_illuminate = ‘P8_7’

# No. of columns and rows of LCD. Following means that the LCD is an 16 X 2
disp_cols = 16
disp_rows = 2

# Initialization of the LCD
LCD = Disp.Adafruit_CharLCD(disp_rs, disp_en, disp_d4, disp_d5, disp_d6, disp_d7,
disp_cols, disp_rows, disp_illuminate)

#Display Hello World message
LCD.message(‘Hello world!’)
# If you need you can print two line message LCD.message(‘Hello\nworld!’)

# Wait 5 seconds
time.sleep(5.0)

# Clear the LCD screen.
LCD.clear()
