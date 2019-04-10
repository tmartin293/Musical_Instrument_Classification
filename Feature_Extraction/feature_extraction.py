"""
Here is my implementation of the referrence project's approach in Python
"""
import numpy as np
import csv
import os
from scipy.io import wavfile
from scipy.fftpack import dct, idct
from numpy import empty_like
    
def WriteToCSV(csv_filename, data):
    with open(csv_filename, mode='a') as data_file:
        csv_writer = csv.writer(data_file, delimiter=',')
        csv_writer.writerow(data)

# Read file
def ReadWav(filename):
    rate, data = wavfile.read(filename)
    # unpack the data
    if data.dtype == np.int16:
        data = data.astype(np.float32) / np.iinfo(np.int16).max
    return data

# Normalize sampled data (remove abs( sample ) <= 0.009)
def RemoveSilence(data):
    # find indexes of silence
    s_index = []
    for i in range(0, len(data)):
        if np.fabs(data[i]) <= 0.009:
            s_index.append(i)
    # remove all index of data that is in s_index
    return np.delete(data, s_index)

# Transform data into 
def MFCC(data):
    # Split the data into 50 segments (44,100 / 50 = 882)
    win_size = 882
    num_frames = int( np.floor(len(data)/ win_size) )
    # Compute the N-point symmetric Hamming window filter (win_size = 882)
    w = np.hamming(win_size)
    # copy data to for use in filtering, leaving the original data unfiltered
    data_new = data
    fourier = np.zeros([len(data)])
    # For each frame
    for i in range(1, num_frames):
        # Calculate the start and end index of the frame
        win_s = range( ((i - 1) * win_size), (i * win_size) )
        # Apply the Hamming Filter to a frame of the normalized sample data
        f_data = np.multiply(data_new[win_s], w) # element wise multiplication
        # Take the DCT of the filtered data
        fourier[win_s] = GetDCT(f_data)
    # Keep first 13 coefficients
    data = GetIDCT(fourier)
    return data[0:12]

# Calculate the Discrete Cosine Transform
def GetDCT(x):
    # "For a single dimension array x, dct(x, norm='ortho') is equal to MATLAB dct(x)"
    dct_t = None
    try:
        # Calculate the DCT of the current frame of normalized data
        dct_t = dct(x, norm='ortho')
    except:
        print("dct failed.")
    return dct_t
        
# Calculate the inverse discrete cosine transform of the transformed data
def GetIDCT(x):
    # "For a single dimension array x, idct(x, norm='ortho') is equal to MATLAB idct(x)"
    idct_t = None
    try:
        # Take the logarithm of all the DCT data
        l_x = np.log(np.fabs(x))
        # Take the IDCT of l_x
        idct_t = idct(l_x + 0.1, norm='ortho')
    except:
        print("idct failed.")
    return idct_t

def main():
    label = 0
    csv_filename = 'test.csv'
    # For each file and sub directory in specified folder
    for root, dirs, files in os.walk('wav/'):
        # parse all the wav files
        for file in files:
            # Build the file name
            filename = os.path.join(root, file)
            if filename.endswith(".wav"):
                # Read .wav file
                data = ReadWav(filename)
                # Normalize and transform data
                data = MFCC( RemoveSilence(data) )
                # Make sure we get the correct size of data
                if len(data >= 13):
                    # Put the appropriate label in the last column
                    data = np.append(data , label)
                    # Append a new row to the specified csv file
                    WriteToCSV(csv_filename, data)
        # End of files in fold; go to next label
        label += 1

main()
