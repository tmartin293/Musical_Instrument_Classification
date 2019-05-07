import Adafruit_CharLCD as LCD
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

"""
1602A LCD
"""
class BBB_LCD:
        def __init__(self):
                self.lcd = LCD.Adafruit_CharLCD('P8_8', 'P8_10', 'P8_18', 'P8_16', 'P8_14', 'P8_12',  16, 2, 'P8_7')
                # Max possible strings
                self.max_disp    =   "1234567890123456\n1234567890123456"
                # Audio Streaming strings
                self.mic_err     =   "Failed to\nConnect to Mic\n"
                self.record_err  =   "Failed to\nSave Audio\n"
                self.len_err     =   "Recording Length\nExceeded\n"
                # Preprocessing strings
                self.mfcc_err    =   "Failed to\nPreprocess Audio\n"
                # ML
                self.predict_err =   "Failed to Guess\nInstrument\n"
                # Correct Output
                self.results     =   "Instrument =\n"
                self.instruments = [ "Cello\n", "Clarinet\n", "Flute\n",
                        "Guitar\n", "Saxophone\n", "Trumpet\n",
                        "Violin\n"]

        def print(self,msg):
                self.lcd.message(msg)

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
                self.base_freq = 10000

        def SetRed(self):
                self.ClearLEDs()
                ToggleLED(0)
        
        def SetGreen(self):
                self.ClearLEDs()
                ToggleLED(1)

        def SetBlue(self):
                self.ClearLEDs()
                ToggleLED(2)
        
        def SetPWM(self,index,new_dc,new_freq):
                PWM.set_duty_cycle(self.colors[0][index],new_dc)
                PWM.set_frequency(self.colors[0][index],new_freq)

        def StartPWM(self,index,new_dc,new_freq):
                PWM.start(self.colors[0][index],new_dc,new_freq,0)
                self.colors[1][index] = True
        
        def StopPWM(self,index):
                PWM.stop(self.colors[0][index])
                self.colors[1][index] = False

        def ToggleLED(self,led):
                if led >= 0 and led <= 2:
                        if self.colors[1][led]:
                                self.StopPWM(led)
                        else:
                                self.StartPWM(led, 100, self.base_freq)

        def ClearLEDs(self):
                for i in range(0,len(self.colors[1])):
                        if self.colors[1][i]:
                                self.StopPWM(i)

        def Cleanup(self):
                self.ClearLEDs()
                PWM.cleanup()
                GPIO.cleanup()                
