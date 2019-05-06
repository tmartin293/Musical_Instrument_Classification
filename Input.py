
import Adafruit_BBIO.GPIO as GPIO
import pyaudio
import datetime
import wave
import time


def button_setup(button = 'P8_17',bounce = 5):

	# setup button for input
	GPIO.setup(button,GPIO.IN)
	GPIO.add_event_detect(button,GPIO.RISING,bouncetime=bounce)


def button_pressed(button = 'P8_17'):
	
	if(GPIO.event_detected(button)):
		return(True)

	else:
		return(False)	


def mic_setup(audio):

	# setup microphone
	mic_str = "AmazonBasics Portable USB Mic"
	index = -1

	for i in range(audio.get_device_count()):
		test_str = audio.get_device_info_by_index(i).get('name')
		if(test_str.startswith(mic_str)):
			index = i
			break

	return(index)


def start_stream(audio,device_index,sample_rate = 44100,audio_format = pyaudio.paInt16,\
	             audio_channel = 1,chunk = 8192):

	return(audio.open(format = audio_format,rate = sample_rate, \
	                  channels = audio_channel,input_device_index = device_index, \
	                  input = True,frames_per_buffer = chunk))


def save_audio(frames,audio,stream,audio_channel = 1,sample_rate = 44100,\
	           audio_format = pyaudio.paInt16):

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


def exit_input(audio):

	GPIO.cleanup()
	audio.terminate()