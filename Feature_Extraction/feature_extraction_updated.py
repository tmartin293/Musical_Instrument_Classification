
import csv
import os
import scipy
import librosa
import numpy as np


def main():
    label = 0
    sample_rate = 44100
    n_fft = int(sample_rate/50)
    hop = int(n_fft/2)
    mfcc_size = 20
    top_db_limit = 35
    csv_filename = 'mfcc_results.csv'
    all_data = np.empty([1,mfcc_size])
    # For each file and sub directory in specified folder
    for root, dirs, files in os.walk("."):
        # parse all the wav files
        for file in files:
            # Build the file name
            filename = os.path.join(root,file)
            if(filename.endswith(".wav")):
                
                # Read .wav file
                data,sample_rate = librosa.load(filename,sr=sample_rate)
                # Remove silence
                data,index = librosa.effects.trim(data,top_db=top_db_limit)
                # Extract MFCC values
                mfcc = librosa.feature.mfcc(data,sr=sample_rate,n_fft=n_fft,\
                                            hop_length=hop,n_mfcc=mfcc_size)
                # Average all MFCC values across entire audio file to get
                # single vector
                mfcc = np.mean(mfcc[1:,:],axis=1)
                # Put the appropriate label in the last column
                mfcc = np.append(mfcc, label)
                mfcc = np.reshape(mfcc,[-1,mfcc_size])

                all_data = np.append(all_data,mfcc,axis=0)
        # End of files in folder; go to next label
        label += 1
    # Save data to .csv file    
    np.savetxt(csv_filename,all_data[1:,:],fmt='%10.8f',delimiter=',')

main()
