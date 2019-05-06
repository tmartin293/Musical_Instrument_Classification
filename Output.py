import Adafruit_CharLCD as LCD
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

"""
1602A LCD
"""
lcd = init_lcd()
# Max possible strings
max_disp    =   "1234567890123456\n1234567890123456"
# Audio Streaming strings
mic_err     =   "Failed to\nConnect to Mic\n"
record_err  =   "Failed to\nSave Audio\n"
len_err     =   "Recording Length\nExceeded\n"
# Preprocessing strings
mfcc_err    =   "Failed to\nPreprocess Audio\n"
# ML
predict_err =   "Failed to Guess\nInstrument\n"
# Correct Output
results     =   "Instrument =\n"
instruments = [ "Cello\n", "Clarinet\n", "Flute\n",
                "Guitar\n", "Saxophone\n", "Trumpet\n",
                "Violin\n"]

def init_lcd(lcd_rs = 'P8_8', lcd_en = 'P8_10', lcd_d4= 'P8_18', 
            lcd_d5 = 'P8_16', lcd_d6 = 'P8_14', lcd_d7 = 'P8_12',
            lcd_columns = 16, lcd_rows = 2, lcd_backlight = 'P8_7'):
    return LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                lcd_columns, lcd_rows, lcd_backlight)
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
SMD RGB LED
"""
colors = init_led()
base_freq = 10000

def init_led(led_red = "P8_9", led_green = "P8_11", led_blue = "P8_15"):
    return [[led_red, led_green, led_blue],[False, False, False]]
    
def SetPWM(index,new_dc,new_freq):
    PWM.set_duty_cycle(colors[0][index],new_dc)
    PWM.set_frequency(colors[0][index],new_freq)

def StartPWM(index,new_dc,new_freq):
    PWM.start(colors[0][index],new_dc,new_freq,0)
    colors[1][index] = True
    
def StopPWM(index):
    PWM.stop(colors[0][index])
    colors[1][index] = False

def LEDAllOff():
    for i in range(0,len(colors[1])):
        if(colors[1][i]):
            StopPWM(i)

def EndAll():
    LEDAllOff()
    PWM.cleanup()
    GPIO.cleanup()
