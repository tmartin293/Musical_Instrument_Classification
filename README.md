
# Musical_Instrument_Classification
Musical Instrument Classification Project Using Beaglebone Black (CSUEB CMPE 344 Class)

* Download and install Debian 9.5 2018-10-07 4GB SD LXQT OS image from https://beagleboard.org/latest-images and move it to a MicroSD card (16 GB minimum recommended size). *

* Follow instructions on http://www.ofitselfso.com/BeagleNotes/Disabling_The_EMMC_Memory_On_The_Beaglebone_Black.php to disable booting from the Beaglebone's EMMC and force booting from the MicroSD card by default. *

* To extend filesystem on MicroSD card: 
1. cd /opt/scripts/tools
2. ./grow_partition.sh
*


* Instructions to install required software on Beaglebone Black to Conda virtual environment: 
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
*


* Process for Developing Machine Learning Model:
Stage 1 – Preprocessing
1. Convert files from .mp3 to .wav

Stage 2 – Feature Extraction
1. Remove leading and trailing silence
2. Extract MFCC values and append instrument label 
3. Save all data to .csv file

Stage 3 – Training (Scikit-Learn SVM)
1. C-Support Vector Classification
   1. C = 50
   2. kernel = 'rbf'
   3. gamma = 0.001
   4. decision_function_shape = 'ovr'

Stage 4 – Testing
1. 75/25 train-test split to prevent overfitting and determine model statistics (accuracy, precision, recall, and F1)

Stage 5 – Model Persistence
1. Serialize SVM model with pickle and deserialize when needed for consistent instrument classifications
*