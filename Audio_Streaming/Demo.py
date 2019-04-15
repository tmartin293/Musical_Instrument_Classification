
import Adafruit_BBIO.GPIO as GPIO
from scipy.io.wavfile import read
from scipy.fftpack import dct, idct
from numpy import empty_like
import numpy as np
import pyaudio
import datetime
import pickle
import math
import wave
import sys
import time


def button_setup(button):

	# setup button for input
	GPIO.setup(button,GPIO.IN)
	GPIO.add_event_detect(button,GPIO.RISING)


def mic_setup(audio):

	# setup microphone
	mic_str = "AmazonBasics Portable USB Mic"
	channel = -1

	for i in range(audio.get_device_count()):
		test_str = audio.get_device_info_by_index(i).get('name')
		if(test_str.startswith(mic_str)):
			channel = i
			break

	return(channel)	


def import_ml_model(model_name):

	with open(model_name, 'rb') as file:
		model = pickle.load(file)
	

	return(model)		


def save_audio(frames,audio,stream,sample_rate,audio_channel,audio_format):

	stream.stop_stream()
	stream.close()

	now = datetime.datetime.now()
	file_name = "audio_test_" + str(now.month) + "-" + str(now.day) + "-" + \
                str(now.year) + "__" + str(now.hour) + "-" + str(now.minute) + \
                "-" + str(now.second) + "_.wav"

	wavefile = wave.open(file_name,'wb')
	wavefile.setnchannels(audio_channel)
	wavefile.setsampwidth(audio.get_sample_size(audio_format))
	wavefile.setframerate(sample_rate)
	wavefile.writeframes(b''.join(frames))
	wavefile.close()

	return(file_name)


def get_mfcc(file_name):

	rate,data = read(file_name)
	if(data.dtype == np.int16):
		data = data.astype(np.float32) / np.iinfo(np.int16).max

	data_size = len(data)
	num_points = 882
	num_frames = math.floor(data_size/num_points)
	filters = np.hamming(num_points)

	data_cpy = data
	fourier = empty_like(data)
	for i in range(1,num_frames):
		window = range(((i-1)*num_points),(i*num_points))
		filter_data = np.multiply(data_cpy[window],filters)
		fourier[window] = dct(filter_data,norm='ortho')

	inv_transform = idct(np.log(abs(fourier)+0.1),norm='ortho')
	result = inv_transform[0:13]
	result = np.reshape(result,(1,-1))

	return(result)


def predict_instrument(model_prediction):

	# Dictionary of possibe instrument predictions
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
	return(switch.get(model_prediction,"N/A"))			


def exit(audio):

	GPIO.cleanup()
	audio.terminate()


def main():

	button = "P8_8"
	model_name = "pickle_model.pkl"
	sample_rate = 44100
	audio_format = pyaudio.paInt16
	audio_channel = 1
	chunk = 4096
	frames = []
	audio = pyaudio.PyAudio()
	counter = 0

	# Setup button and microphone
	button_setup(button)
	model = import_ml_model(model_name)
	device_index = mic_setup(audio)

	# If unable to connect to the microphone; exit
	if(device_index == -1):
		print("Unable to connect to microphone, exiting ...")
		exit(audio)
		sys.exit()

	print("Ready")	

	# Allows counter number of audio recordings before exit
	while(counter < 1):

		time.sleep(0.05)

		# Begin recording
		if(GPIO.event_detected(button)):
			print("Recording")
			stream = audio.open(format = audio_format,rate = sample_rate, \
	                 channels = audio_channel,input_device_index = device_index, \
	                 input = True,frames_per_buffer = chunk)

			# Collect data until button pressed again
			while(not GPIO.event_detected(button)):
				data = stream.read(chunk)
				frames.append(data)

			file_name = save_audio(frames,audio,stream,sample_rate,audio_channel,audio_format)
			print("Audio stream saved to file: ",file_name)
			frames = []
			counter = counter + 1

			try:
				mfcc = get_mfcc(file_name)
				print("Classified instrument: ",predict_instrument(model.predict(mfcc)[0]))

			except:
				print("Classified instrument: N/A (Error)")
				print(mfcc)

	exit(audio)
	print("Demo completed")



main()

