import librosa
from scipy.fft import fft
import numpy as np


def extract_peak_frequency(data, sampling_rate):
    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(data))

    peak_coefficient = np.argmax(np.abs(fft_data))
    peak_freq = freqs[peak_coefficient]

    return abs(peak_freq * sampling_rate)


#  As always clean this up this is a crime
def decode(bin):
    decoded = ""
    lv = 3
    pulse_count = 0
    for i in bin:
        if i != lv:
            decoded += i
            lv = i
        else:
            pass
    return decoded.replace('_', '')


#  Who knows how this works Python is shitty
def space(string):
    chunk = 8
    return str(' '.join([string[i:i + chunk] for i in range(0, len(string), chunk)]))


def binToText(bin):
    output = ""
    bytes = bin.split(' ')
    for b in bytes:
        output += chr(int(b[:8], 2))
    return output


filename = "/home/gabrieltower/Documents/GitHub/AmMod/modulator/path_of_file.wav"

sr = librosa.get_samplerate(filename)

stream = librosa.stream(filename, block_length=10, frame_length=10, hop_length=1024)

demodulated_text = ""

for frame in stream:
    peak_freq = int(extract_peak_frequency(frame, sr))
    if peak_freq == 1000:
        demodulated_text += "1"
    elif peak_freq == 500:
        demodulated_text += "0"
    elif peak_freq == 750:
        demodulated_text += "_"
    else:
        demodulated_text += ""


print(binToText(space(decode(demodulated_text))))
