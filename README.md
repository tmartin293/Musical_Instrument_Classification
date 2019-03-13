# Musical_Instrument_Classification
Musical Instrument Classification Project Using Beaglebone Black (CSUEB CMPE 344 Class)

To extend filesystem on MicroSD Card: 
1) cd /opt/scripts/tools
2) ./grow_partition.sh

Process:

Stage 1 – Preprocessing
1. Musical Instrument Signal
  1. Convert / Save to .wav
  2. Digitalize the input signal
  3. Signal amplitude normalization
  4. Silence removal

Stage 2 – Feature Extraction
1. Pre-Processing
  1. MFCC
  2. Using DFT and identifying the most predominant frequencies with the greatest percentage contribution to the total power of the signal


Stage 3 – Training
1. Feature Extraction
  1. Try various classification techniques


Stage 4 – Testing
1. Classification


Stage 5 – Predictions
1. Testing
