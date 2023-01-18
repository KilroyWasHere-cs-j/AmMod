import librosa
import numpy as np
from scipy.signal import butter, sosfilt, sosfreqz
import time
import sys
from itertools import groupby

start_time = 0
stop_time = 0

filename = "/home/gabetower/Git/AmMod/modulator/path_of_file.wav"

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


def extract_peak_frequency(data, sampling_rate):
    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(data))

    peak_coefficient = np.argmax(np.abs(fft_data))
    peak_freq = freqs[peak_coefficient]

    return abs(peak_freq * sampling_rate)


def list_To_String(list):
    return "".join(list)


def decode_To_Text(dt):
    dt = ["".join(g) for k, g in groupby(dt) if k != '_']  #
    dt = [x[0] for x in dt]
    dt = (''.join(dt))
    return list_To_String(binToText(space(dt)))


#  Who knows how this works Python is shitty
#  But it breaks the string up into blocks of 8
def space(string):
    chunk = 8
    return str(' '.join([string[i:i + chunk] for i in range(0, len(string), chunk)]))


#  Converts text into binary
def binToText(bin):
    bytes = bin.split(' ')
    return [chr(int(b[:8], 2)) for b in bytes]


def main(path):
    sr = librosa.get_samplerate(filename)

    stream = librosa.stream(filename, block_length=10, frame_length=10, hop_length=1024)

    demodulated_text = str()

    for frame in stream:
        sig = butter_bandpass_filter(frame, lowpass, highpass, sr, order)
        peak_freq = int(extract_peak_frequency(sig, sr))
        demodulated_text = "".join([demodulated_text, "1"]) if peak_freq == 1000 else "".join([demodulated_text, "0"]) if peak_freq == 500 else "".join([demodulated_text, "_"]) if peak_freq == 750 else "".join([demodulated_text, ""])
    print(decode_To_Text(demodulated_text))
    stop_time = time.perf_counter()

    print((stop_time - start_time))

if __name__ == "__main__":
    start_time = time.perf_counter()
    main(filename)
