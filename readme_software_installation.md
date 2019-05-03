
1. Follow instructions at https://jamwheeler.com/college-productivity/using-a-raspberry-pi-for-instrumentation-software-part-3/
   to setup and install:
   - Miniconda3
   - Add rpi channel to conda
   - Create & activate a python 3.6 conda environment
     * conda create -n py36 python=3.6
     * source activate py36

2. conda install -c rpi scipy 

3. conda install -c rpi scikit-learn 

4. conda install --channel=numba llvmlite

5. conda install -c rpi openblas 

6. pip install numpy

7. pip install librosa==0.6.2

8. pip install pyaudio

9. pip install Adafruit_BBIO

10. pip install Adafruit-CharLCD