
import pyaudio

def connect_mic(audio):

	mic_str = "AmazonBasics Portable USB Mic"
	channel = -1

	for i in range(audio.get_device_count()):
		test_str = audio.get_device_info_by_index(i).get('name')
		if(test_str.startswith(mic_str)):
			channel = i
			break

	return(channel)





