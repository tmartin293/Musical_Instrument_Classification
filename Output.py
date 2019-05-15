import Adafruit_CharLCD as LCD
import Adafruit_BBIO.GPIO as GPIO

"""
1602A LCD
"""
class CharLCD:
        def __init__(self):
                self.lcd = LCD.Adafruit_CharLCD('P8_8', 'P8_10', 'P8_18', 'P8_16', 'P8_14', 'P8_12',  16, 2, 'P8_26')

        def print(self,msg):
                self.clear()
                self.lcd.message(msg)
                  
        def mic_err(self):
                self.print("Failed to\nConnect to Mic\n")

        def rec_error(self):
                self.print("Failed to\nSave Audio\n")
                
        def len_error(self):
                self.print("Recording Length\nExceeded\n")

        def clear(self):
                self.lcd.clear()

        def Cleanup(self):
                self.clear()
                GPIO.cleanup()
