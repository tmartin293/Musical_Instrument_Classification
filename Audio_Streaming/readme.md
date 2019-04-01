
Steps for installing pyaudio and other audio processing tools on Beaglebone Black:

1. Add following lines to sources.list file in: /etc/apt/ folder
	deb  http://deb.debian.org/debian  stretch main
	deb-src  http://deb.debian.org/debian  stretch main

2. apt-get update

3. sudo apt‐get install mplayer alsa‐utils libav‐tools

4. sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

5. sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

6. sudo apt-get install ffmpeg libav-tools

7. pip3 install pyaudio


