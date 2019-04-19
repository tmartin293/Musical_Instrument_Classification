This will be used to output our results to the 1602A LCD screen using Adafruit's CharLCD Library.


Tutorial on 1602A LCD for the Beaglebone Black found at the following site:  

cd /opt/scripts/tools

sudo ./grow_partition.sh

sudo -H pip3 install Adafruit_BBIO

sudo -H pip3 install Adafruit_CharLCD

alias python=python3

python lcd_test.py

http://www.linoroid.com/2016/10/connecting-16x2-character-lcd-to-beaglebone-black/
