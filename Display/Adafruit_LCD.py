"""
Based on the tutorial from Adafruit: 
https://github.com/adafruit/Adafruit_Python_CharLCD/blob/master/examples/char_lcd.py
"""
import Adafruit_CharLCD as LCD

# BeagleBone Black configuration:
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



# Some strings to work with
max_disp    =   "1234567890123456\n1234567890123456"
# Audio Streaming
mic_err     =   "Failed to\nConnect to Mic\n"
record_err  =   "Failed to\nSave Audio\n"
len_err     =   "Recording Length\nExceeded\n"
# Preprocessing
mfcc_err    =   "Failed to\nPreprocess Audio\n"
# ML
predict_err =   "Failed to Guess\nInstrument\n"
# Correct Output
results     =   "Instrument =\n"
instruments = [ "Cello\n", "Clarinet\n", "Flute\n",
                "Guitar\n", "Saxophone\n", "Trumpet\n",
                "Violin\n"]
def lcd_print(msg):
    LCD.message(msg)

def lcd_clear():
    LCD.clear()

def print_inst(num):
    if(num < len(instruments) and num > len(instruments)):
        lcd_print("Wrong Instrument\nDetected\n")
    else:
        lcd_print(results + instruments[num])