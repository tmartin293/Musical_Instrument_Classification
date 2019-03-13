# Musical_Instrument_Classification
Musical Instrument Classification Project Using Beaglebone Black (CSUEB CMPE 344 Class)

To extend filesystem on MicroSD Card: 
1) cd /opt/scripts/tools
2) ./grow_partition.sh

Process:

#H1 Stage 1 – Preprocessing
o	Musical Instrument Signal
	Convert / Save to .wav
	Digitalize the input signal
	Signal amplitude normalization
	Silence removal


#H1 Stage 2 – Feature Extraction
o	Pre-Processing
	MFCC
	Using DFT and identifying the most predominant frequencies with the greatest percentage contribution to the total power of the signal


#H1 Stage 3 – Training
o	Feature Extraction
	Try various classification techniques


#H1 Stage 4 – Testing
o	Classification


#H1 Stage 5 – Predictions
o	Testing
