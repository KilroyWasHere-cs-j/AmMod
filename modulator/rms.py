# This script is used to visualize the audio file
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, sosfreqz

lowpass = 500
highpass = 1000
order = 10

def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='band', output='sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        sos = butter_bandpass(lowcut, highcut, fs, order=order)
        y = sosfilt(sos, data)
        return y

y, sr = librosa.load("path_of_file.wav")

y = butter_bandpass_filter(y, lowpass, highpass, sr, order)
rmss = librosa.feature.rms(y=y)
print("Raw rmss {0}".format(rmss))