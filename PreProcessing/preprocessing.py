"""
preprocessing.py
CMPE 344
"""
import os
from pydub import AudioSegment

# Convert all MP3 files to Wav in the same directory
def MP3toWAV(rootdir):
    # traverse each directory
	for root, dirs, files in os.walk(rootdir):
        # traverse each file in directory
		for file in files:
			filepath = os.path.join(root,file)
			if(filepath.endswith(".mp3")):
				song = os.path.splitext(file)[0]
				src = os.path.join(root,song + ".mp3")
				dst = os.path.join(root,song + ".wav")
				try:
					AudioSegment.from_mp3(src).export(dst, format="wav")
				except:
					pass	

                      
# Put the "Musical Instrument Sound Samples" directory in the same folder
# to convert them all to wav files
MP3toWAV(".")
