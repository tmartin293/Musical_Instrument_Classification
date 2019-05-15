
import scipy
import pickle
import librosa
import time
import numpy as np


class Predict:
    def __init__(self, lcd):
        self.lcd = lcd
        self.sample_rate = 44100
        self.top_db_limit = 35
        self.hop = int(44100/100)
        self.n_fft = int(44100/50)
        self.mfcc_size = 14
        self.switch = {
            1: "Cello",
            2: "Clarinet",
            3: "Flute",
            4: "Guitar",
            5: "Saxophone",
            6: "Trumpet",
            7: "Violin",
        }
        # Import Pickle Model
        with open("pickle_model.pkl", 'rb') as file:
            self.model = pickle.load(file)

    # Dictionary of possibe instrument predictions
    def instrument_prediction(self, prediction):
        # Return instrument or N/A if the input is not in the dictionary
        return self.switch.get(prediction,"N/A")

    def get_predictions(self,filename):
        # Load audio
        data,sample_rate = librosa.load(filename,sr=self.sample_rate)
        if len(data) <= self.n_fft:
            self.lcd.print("Data Error\nTry Again\n")
            time.sleep(1)
            return []
            
        # Trim with a threshold of 35
        data,index = librosa.effects.trim(data,top_db=self.top_db_limit,frame_length=self.n_fft,hop_length=self.hop)
        # Locate note onset events in each frame
        onset_frames = librosa.onset.onset_detect(y=data,sr=sample_rate,hop_length=self.hop)
        # Calculate the number of notes
        notes = self.hop * onset_frames
        predictions = []
        # Predict instrument for each detected note
        for i in range(0, len(notes)):
            if i < (len(notes)-1):
                note_data = data[notes[i]:notes[i+1]]
            else:
                note_data = data[notes[i]:-1]
            # Mel-frequency cepstral coefficients
            mfcc = librosa.feature.mfcc(note_data,sr=sample_rate,n_fft=self.n_fft,hop_length=self.hop,n_mfcc=self.mfcc_size)
            mfcc = np.mean(mfcc[1:,:],axis=1)
            mfcc = np.reshape(mfcc,(1,-1))
            result = self.model.predict(mfcc)[0]
            predictions.append(result)
        # Determine prediction accuracy for each instrument detected
        result_strs = []
        unique,counts = np.unique(predictions,return_counts=True)
        indices = np.argsort(counts)
        indices = np.flip(indices,0)
        unique = unique[indices]
        counts = counts[indices]
        # Calculate the accuracy percents
        for i in range(0,len(unique)):
            accuracy = (counts[i] / len(predictions)) * 100
            prediction_str = self.instrument_prediction(unique[i]) + "\n{:3.3f}".format(accuracy) + "%\n"
            result_strs.append(prediction_str)
        return result_strs