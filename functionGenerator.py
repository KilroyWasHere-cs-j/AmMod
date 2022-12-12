import numpy as np
from scipy.io.wavfile import write
from playsound import playsound

signal_duration = 0.5

dit_freq = 1000
dah_freq = 400


def dit():
    sine(dit_freq, signal_duration)


def dah():
    sine(dah_freq, signal_duration)


def sine(freq, duration):
    sps = 44100
    samples = np.arange(duration * sps)
    wavefrom = np.sin(2 * np.pi * samples * freq / sps)
    wavefrom_ints = np.int16(wavefrom * 32767)
    write('hold.wav', sps, wavefrom_ints)
    playsound('hold.wav')

