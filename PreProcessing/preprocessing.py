"""
preprocessing.py
Microprocessing Lab
Group 5
Created by Daniel on 3/22/19.
"""
import os
from pydub import AudioSegment

# Conver all MP3 files to Wav in a directory
def MP3toWAV(rootdir):
    # traverse each directory
    for subdir, files in os.walk(rootdir):
        # traverse each file in directory
        for file in files:
            filepath = subdir + os.sep + file
            # if .mp3, then convert to .wav
            if filepath.endswith(".mp3"):
                # separate the file's name
                song = os.path.splitext(file)[0]
                src = subdir + os.sep + song + ".mp3"
                dst = subdir + os.sep + song + ".wav"
                AudioSegment.from_mp3(src).export(dst, format="wav")
# Put the "Musical Instrument Sound Samples" directory in the same folder
# to convert them all to mp3s
MP3toWAV(".")
