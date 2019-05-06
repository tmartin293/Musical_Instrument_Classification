
import Adafruit_BBIO.GPIO as GPIO
import pyaudio
import datetime
import wave
import time

class Button:
    def __init__(self):
        self.button = 'P8_17'
        self.bounce = 5

    def button_setup(self):
        # setup button for input
        GPIO.setup(self.button,GPIO.IN)
        GPIO.add_event_detect(self.button,GPIO.RISING,bouncetime=self.bounce)

    def button_pressed(self):
        """ From the Adafruit_BBIO Library,
        "Returns True if an edge has occured on a given GPIO. You need to 
        enable edge detection using add_event_detect() first. Pin should be 
        type IN.". Since the function call returns a Boolean, no need for if-else
        """
        return(GPIO.event_detected(self.button))

class Mic:
    def __init__(self):
        self.mic_str = "AmazonBasics Portable USB Mic"

    def mic_setup(self,audio):
        # setup microphone
        for i in range(audio.get_device_count()):
            test_str = audio.get_device_info_by_index(i).get('name')
            if(test_str.startswith(self.mic_str)):
                return(i)
        return(-1)


    def start_stream(self,audio,device_index,sample_rate = 44100,audio_format = pyaudio.paInt16,\
                    audio_channel = 1,chunk = 8192):
        return(audio.open(format = audio_format,rate = sample_rate, \
                        channels = audio_channel,input_device_index = device_index, \
                        input = True,frames_per_buffer = chunk))


    def save_audio(self,frames,audio,stream,audio_channel = 1,sample_rate = 44100,\
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

    def exit_input(self,audio):
        GPIO.cleanup()
        audio.terminate()
