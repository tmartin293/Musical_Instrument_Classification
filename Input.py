
import Adafruit_BBIO.GPIO as GPIO
import Output
import pyaudio
import datetime
import wave
import time

class Button:
    def __init__(self):
        self.button = 'P8_17'
        self.bounce = 5
        self.button_setup()

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
        return GPIO.event_detected(self.button)

    def cleanup(self):
        GPIO.cleanup()


class Mic:
    def __init__(self, lcd):
        self.mic_str = "AmazonBasics Portable USB Mic"
        self.audio = pyaudio.PyAudio()
        self.device_index = self.mic_setup()
        if(self.device_index == -1):
            lcd.print("Unable to connect to microphone.")
            self.audio.terminate()
        self.sample_rate = 44100
        self.audio_format = pyaudio.paInt16
        self.audio_channel = 1
        self.chunk = 8192
        self.frames = []
        self.stream = None
        self.counter = 0

    def mic_setup(self):
        for i in range(self.audio.get_device_count()):
            test_str = self.audio.get_device_info_by_index(i).get('name')
            if test_str.startswith(self.mic_str):
                return i
        return -1

    # Instead of returning the stream, initialize the object's variable to the stream
    def start_stream(self,audio_format = pyaudio.paInt16):
        self.stream = self.audio.open(format = self.audio_format,rate = self.sample_rate, \
                          channels = self.audio_channel,input_device_index = self.device_index, \
                          input = True, frames_per_buffer = self.chunk)

    # Do we really need to return the filename? I think a new system should be implemented which
    # deals with audio files in some way
    def save_audio(self, audio_format = pyaudio.paInt16):
        self.stream.stop_stream()
        self.stream.close()
        file_name = "audio_test_" + datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S") + "_.wav"
        wavefile = wave.open(file_name,'wb')
        wavefile.setnchannels(self.audio_channel)
        wavefile.setsampwidth(self.audio.get_sample_size(audio_format))
        wavefile.setframerate(self.sample_rate)
        wavefile.writeframes(b''.join(self.frames))
        wavefile.close()
        return file_name 

    def cleanup(self):
        self.audio.terminate()
