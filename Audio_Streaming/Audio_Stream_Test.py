import datetime
import pyaudio
import wave
import sys
import connect_mic

now = datetime.datetime.now()
sample_rate = 44100
audio_format = pyaudio.paInt16
audio_channel = 1
chunk = 4096
record_time = 3
frames = []

file_name = file_name = "audio_test_" + str(now.month) + "-" + str(now.day) + \
            "-" + str(now.year) + "__" + str(now.hour) + "-" + str(now.minute) + \
            "-" + str(now.second) + "_.wav"

audio = pyaudio.PyAudio()
device_index = connect_mic.connect_mic(audio)

if(device_index == -1):
	audio.terminate()
	sys.exit()

stream = audio.open(format = audio_format,rate = sample_rate,channels = audio_channel, \
	                input_device_index = device_index,input = True, \
	                frames_per_buffer = chunk)

print("Recording...")

for i in range(0,int((sample_rate/chunk)*record_time)):
	data = stream.read(chunk)
	frames.append(data)

print("Finished Recording.")


stream.stop_stream()
stream.close()
audio.terminate()

wavefile = wave.open(file_name,'wb')
wavefile.setnchannels(audio_channel)
wavefile.setsampwidth(audio.get_sample_size(audio_format))
wavefile.setframerate(sample_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
