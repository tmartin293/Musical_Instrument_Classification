import Input
import Output
import Prediction

"""
Configuration
"""
# Setup Compenents
lcd = Output.BBB_LCD()
button = Input.Button()
led = Output.LED()
mic = Input.Mic(lcd)
predict = Prediction.Predict(lcd)

# Display Setup
# stretch goal: add a cool graphic loading message
lcd.print("Loading...")

predict.import_ml_model()

"""
Event Loop
"""
# Prompt user to 'Press Button' to record
lcd.print("Press Button To\nStart Recording\n")
while True:
    # On Event Dected
    if button.is_pressed():
        # Record Audio
        mic.start_stream()
        # Change color to Green
        led.SetGreen()

# Prompt user to 'Press Button' to stop recording recording
lcd.print("Press Button To\nStart Recording\n")
while True:
    # On Event Detected
    if(button.button_pressed()):
        # Stop Recording Audio
        mic.start_stream()
        # Change color to Red
        led.red()

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
