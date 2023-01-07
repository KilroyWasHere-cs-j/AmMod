# imports
import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy.io import wavfile

BIN_SIZE = 20


def conv(signal):
    pass


def audio_array(path):
    return wavfile.read(path)[1]


# shows the sound waves
def visualize(path: str):
    # reading the audio file
    raw = wave.open(path)
    # reads all the frames
    # -1 indicates all or max frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")

    # gets the frame rate
    f_rate = raw.getframerate()

    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    time = np.linspace(
        0,  # start
        len(signal) * f_rate * 2,
        num=len(signal)
    )

    # using matplotlib to plot
    # creates a new figure
    plt.figure(1)

    # title of the plot
    plt.title("Sound Wave")

    # label of x-axis
    plt.xlabel("Time")

    x = np.fft.fft(signal)
    # actual plotting
    plt.plot(time, signal)

    # shows the plot
    # in new window
    plt.show()

    plt.plot(time, x)
    plt.show()

    print(time)

# you can also save
# the plot using
# plt.savefig('filename')


def extract(w, freqs):
    for coef, freq, in zip(w, freqs):
        if coef:
            pass
            # print('{c:>6} * exp(2 pi i t * {f}'.format(c=coef, f=freq))


if __name__ == "__main__":
    # gets the command line Value
    path = "/Monday at 22-31.wav"
    visualize(path)
    audio_ar = audio_array(path)
    w = np.fft.fft(audio_ar)
    freqs = np.fft.fftfreq(len(w))
    #print(freqs)
    extract(w, freqs)

