"""
Here is my implementation of the referrence project's approach in Python
"""
import numpy as np
import csv
import os
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import dct, idct
from numpy import empty_like
import time
    
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

# Compute the N-point symmetric Hamming window filter (win_size = 882)
def MFCC(data):
    p = 882
    num_frames = int( np.floor(len(data)/p) )
    w = np.hamming(p)
    # Apply the Hamming Filter to the normalized sample data (element wise multiplication)
    data_new = data
    fourier = np.zeros([len(data)])
    for i in range(1, num_frames):
        win_s = range( ((i-1)*p), (i*p) )
        fourier[win_s] = GetDCT( np.multiply(data_new[win_s], w) )
    data = GetIDCT(fourier)
    return data[0:13]

# Calculate the Discrete Cosine Transform of the
def GetDCT(x):
    # "For a single dimension array x, dct(x, norm='ortho') is equal to MATLAB dct(x)"
    dct_t = None
    try:
        dct_t = dct(x, norm='ortho')
    except:
        print("dct failed.")
    return dct_t
        
# Calculate the inverse discrete cosine transform of the transformed data
def GetIDCT(fourier):
    # "For a single dimension array x, idct(x, norm='ortho') is equal to MATLAB idct(x)"
    idct_t = None
    try:
        idct_t = idct(np.log(np.fabs(fourier)+0.1), norm='ortho')
    except:
        print("idct failed.")
    return idct_t

def main():
    label = 0
    csv_filename = 'test.csv'
    for root, dirs, files in os.walk('./testwav/'):
        if label != 0: 
            # parse all the wav files
            for file in files:
                filename = os.path.join(root, file)
                if filename.endswith(".wav"):
                    # Read .wav file
                    data = ReadWav(filename)

                    # normalize and filter data
                    data = MFCC( RemoveSilence(data) )
                             
                    #isolate the first 13 MFCC values and the label
                    if len(data >= 13):
                        data = np.append(data , label)
                        WriteToCSV(csv_filename, data)
        label += 1

main()
