This will work with the folder of preprocessed .wav files.

The normalization algorithm will remove sample values that are outside of the range of [-0.009 .. 0.009]
Then it calculates the first 13 values of the MFCC of the normalized data.

Check out the Example folder for an example of what the process looks like on a single file
