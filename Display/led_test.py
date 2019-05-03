
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time



def EndAll():
    LEDAllOff()
    PWM.cleanup()
    GPIO.cleanup()
    
def SetPWM(index,new_dc,new_freq):
    PWM.set_duty_cycle(colors[index],new_dc)
    PWM.set_frequency(colors[index],new_freq)

def StartPWM(index,new_dc,new_freq):
    PWM.start(colors[index],new_dc,new_freq,0)
    led_on[index] = True
    

def StopPWM(index):
    PWM.stop(colors[index])
    led_on[index] = False

def LEDAllOff():
    for i in range(0,num_colors):
        if(led_on[i]):
            StopPWM(i)


GREEN = "P8_7"
RED = "P8_9"
BLUE = "P8_11"

# frequency in Hz (must be greater than 0)
base_freq = 10000
counter = 0
index = 0
colors = [BLUE,RED,GREEN]
led_on = [False,False,False]
num_colors = len(colors)

StartPWM(0,100,base_freq)
time.sleep(0.05)
StartPWM(1,100,base_freq)
time.sleep(0.05)
StartPWM(2,100,base_freq)
time.sleep(0.05)
EndAll()
