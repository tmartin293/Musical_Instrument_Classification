# Musical_Instrument_Classification
Musical Instrument Classification Project Using Beaglebone Black (CSUEB CMPE 344 Class)

To extend filesystem on MicroSD Card: 
1) cd /opt/scripts/tools
2) ./grow_partition.sh

Process:

Stage 1 – Preprocessing
1. Convert / Save to .wav

Stage 2 – Feature Extraction
1. Silence Removal
2. MFCC 

Stage 3 – Training
1. C-Support Vector Classification
   1. C = 500
   2. kernel = 'rbf'
   3. gamma = 0.001
   4. decision_function_shape = 'ovr'

Stage 4 – Testing
1. Classification

Stage 5 – Predictions
1. Testing
