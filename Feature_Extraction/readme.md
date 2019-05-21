
The feature_extraction_updated script will extract the first 14 MFCC values for all of the .wav files in the current working directory, remove the first MFCC value (sum of log energies), append an integer label to the array of MFCC values repesenting the instrument, and save the results to a .csv file. 


Check out the Librosa_Predictions notebook in the Example folder for an example of what the process looks like on a single file.
