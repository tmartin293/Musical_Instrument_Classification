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
mic = Input.Mic()

# Display Setup
# stretch goal: add a cool graphic loading message
lcd.print("Loading...")
# Import Pickle Model


"""
Event Loop
"""
# Prompt user to 'Press Button' to record
# On Event Dected
    # Record Audio
    # Change color to Green
# Prompt user to 'Press Button' to stop recording recording
# On Event Detected
    # Stop Recording Audio
    # Change color to Red
# Normalization
    # Trim
    # Onset Detection
# Predictions
# Display results

"""
Teardown
"""
# GPIO Cleanup
# Audio Stream Terminate
