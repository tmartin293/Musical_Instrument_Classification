
import Input
import Output
import Prediction

"""
Configuration
"""
# Setup Compenents
lcd = Output.CharLCD()
button = Input.Button()
led = Output.LED()
mic = Input.Mic(lcd)
predict = Prediction.Predict(lcd)

# Display Setup
# stretch goal: add a cool graphic loading message

"""
Event Loop
"""
# Prompt user to 'Press Button' to record
lcd.print("Press Button To\nStart Recording\n")
while True:
    # On Event Detection
    if button.is_pressed():
    	break

# Record Audio
mic.start_stream()
led.SetGreen()
lcd.print("Press Button To\nStop Recording\n")

while not button.is_pressed():
    mic.read_data()
led.SetRed()
mic.save_audio()


# Classify instrument(s) and display results
instruments = predict.get_predictions(mic.filenames[mic.counter-1])
num_instruments = str(len(instruments))
lcd.print("# of possible\ninstruments:" + num_instruments)
time.sleep(1)
for i in range(0,len(instruments)):
	lcd.print(instruments[i])
	time.sleep(1)

"""
Teardown
"""
lcd.Cleanup()
button.cleanup()
led.Cleanup()
mic.cleanup()
