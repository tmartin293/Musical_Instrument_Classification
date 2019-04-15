
import Adafruit_BBIO.GPIO as GPIO
import time

button = "P8_8"
timeout = 100
counter = 0

GPIO.setup(button,GPIO.IN)
GPIO.add_event_detect(button,GPIO.RISING)


while(counter < timeout):
	time.sleep(0.1)
	if(GPIO.event_detected(button)):
		print("Button pressed!")
	counter = counter + 1	


GPIO.cleanup()