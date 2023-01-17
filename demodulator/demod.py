import librosa
import numpy as np
from scipy.signal import butter, sosfilt, sosfreqz

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

# Branching test

#  Who knows how this works Python is shitty
#  But it breaks the string up into blocks of 8
def space(string):
    chunk = 8
    return str(' '.join([string[i:i + chunk] for i in range(0, len(string), chunk)]))


#  Converts text into binary
def binToText(bin):
    output = ""
    bytes = bin.split(' ')
    for b in bytes:
        output += chr(int(b[:8], 2))
    return output

def decodeToText(bin):
    return binToText(space(decode(bin)))


def main(path):
    sr = librosa.get_samplerate(filename)

    stream = librosa.stream(filename, block_length=10, frame_length=10, hop_length=1024)

    demodulated_text = ""

    for frame in stream:
        sig = butter_bandpass_filter(frame, lowpass, highpass, sr, order)
        peak_freq = int(extract_peak_frequency(sig, sr))
        if peak_freq == 1000:
            demodulated_text += "1"
        elif peak_freq == 500:
            demodulated_text += "0"
        elif peak_freq == 750:
            demodulated_text += "_"
        else:
            demodulated_text += ""
    print(decodeToText(demodulated_text))

if __name__ == "__main__":
    main(filename)
