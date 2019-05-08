
import scipy
import pickle
import librosa
import numpy as np


class Predict:
    def __init__(self):
        # Import Pickle Model
        with open("pickle_model.pkl", 'rb') as file:
            self.model = pickle.load(file)

    # Dictionary of possibe instrument predictions
    def instrument_prediction(self, prediction):
        switch = {
            1: "Cello",
            2: "Clarinet",
            3: "Flute",
            4: "Guitar",
            5: "Saxophone",
            6: "Trumpet",
            7: "Violin",
        }
        # Return instrument or N/A if the input is not in the dictionary
        return switch.get(prediction,"N/A")

    def get_predictions(self,filename,sample_rate = 44100,top_db_limit = 35,\
                        hop = int(44100/100),n_fft = int(44100/50),mfcc_size = 14):
        
        data,sample_rate = librosa.load(filename,sr=sample_rate)
        data,index = librosa.effects.trim(data,top_db=top_db_limit)
        onset_frames = librosa.onset.onset_detect(y=data,sr=sample_rate,hop_length=hop)
        notes = hop * onset_frames
        predictions = []

        # Predict instrument for each detected note
        for i in range(0, len(notes)):
            if i < len(notes)-1:
                note_data = data[notes[i]:notes[i+1]]
            else:
                note_data = data[notes[i]:-1]
                
            mfcc = librosa.feature.mfcc(note_data,sr=sample_rate,n_fft=n_fft,hop_length=hop,n_mfcc=mfcc_size)
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
       
        for i in range(0,len(unique)):
            accuracy = (counts[i] / len(predictions)) * 100
            prediction_str = self.instrument_prediction(unique[i]) + "\n{:3.3f}".format(accuracy) + "%\n"
            result_strs.append(prediction_str)
        return(result_strs)




