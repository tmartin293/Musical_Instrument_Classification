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
    # On Event Dected
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

# Normalization
    # Trim
    # Onset Detection
# Predictions
# Display results

"""
Teardown
"""
lcd.Cleanup()
button
led.Cleanup()
mic.exit_input()
predict
