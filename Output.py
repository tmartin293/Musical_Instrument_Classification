import Adafruit_CharLCD as LCD
import Adafruit_BBIO.GPIO as GPIO

"""
1602A LCD
"""
class CharLCD:
        def __init__(self):
                self.lcd = LCD.Adafruit_CharLCD('P8_8', 'P8_10', 'P8_18', 'P8_16', 'P8_14', 'P8_12',  16, 2, 'P8_26')
                # Max possible strings
                self.max_disp    =   "1234567890123456\n1234567890123456"
                # Audio Streaming strings
                self.mic_err     =   "Failed to\nConnect to Mic\n"
                self.record_err  =   "Failed to\nSave Audio\n"
                self.len_err     =   "Recording Length\nExceeded\n"

        def print(self,msg):
                self.clear()
                self.lcd.message(msg)

        def MicError(self):
                self.print(self.mic_err)

        def RecError(self):
                self.print(self.record_err)
                
        def LenError(self):
                self.print(self.len_err)

        def clear(self):
                self.lcd.clear()

        def Cleanup(self):
                self.clear()
                GPIO.cleanup()

"""
SMD RGB LED
"""
class LED:
        def __init__(self):
                # [Red, Green, Blue]
                self.colors = [["P8_9", "P8_7", "P8_11"],[False, False, False]]
                for i in range(0, len(self.colors[0])):
                        GPIO.setup(self.colors[0][i], GPIO.OUT)

        def SetRed(self):
                self.ClearLEDs()
                self.ToggleLED(0)
        
        def SetGreen(self):
                self.ClearLEDs()
                self.ToggleLED(1)

        def SetBlue(self):
                self.ClearLEDs()
                self.ToggleLED(2)

        def ToggleLED(self,led):
                if led >= 0 and led <= 2:
                        if self.colors[1][led]:
                                GPIO.output(self.colors[0][led], GPIO.HIGH)
                        else:
                                GPIO.output(self.colors[0][led], GPIO.LOW)

        def ClearLEDs(self):
                for i in range(0,len(self.colors[1])):
                        if self.colors[1][i]:
                                GPIO.output(self.colors[0][i], GPIO.LOW)

        def Cleanup(self):
                self.ClearLEDs()
                GPIO.cleanup()                
