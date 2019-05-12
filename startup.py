

import Output
lcd = Output.CharLCD()
lcd.print("Loading...")

import time
import Input
import Prediction

"""
Configuration
"""
# Setup Compenents

button = Input.Button()
led = Output.LED()
mic = Input.Mic(lcd)
predict = Prediction.Predict(lcd)

# Display Setup
# stretch goal: add a cool graphic loading message

"""
Event Loop
"""
done = False
count = 0
while not done:
    # Prompt user to 'Press Button' to record
    lcd.print("Press Button To\nStart Recording\n")
    
    button.get_input()
    
    # Record Audio
    mic.start_stream()
    led.SetGreen()
    lcd.print("Press Button To\nStop Recording\n")
    
    while not button.is_pressed():
        mic.read_data()
        
    led.SetRed()
    mic.save_audio()
    lcd.print("Predicting...\n")
    
    
    # Classify instrument(s) and display results
    instruments = predict.get_predictions(mic.filenames[mic.counter-1])
    lcd.print("# of possible\ninstruments:" + str(len(instruments)))
    time.sleep(5)
    for i in range(0,len(instruments)):
        lcd.print(instruments[i])
        time.sleep(5)
    
    if count == 3:
        done = True
    count = count + 1

"""
Teardown
"""
lcd.Cleanup()
button.cleanup()
led.Cleanup()
mic.cleanup()
