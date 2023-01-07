import generator as gen
import pyaudio
import wave
import _thread


# Record in chunks of 1024 samples
chunk = 1024

# 16 bits per sample
sample_format = pyaudio.paInt16
chanels = 2

# Record at 44400 samples per second
smpl_rt = 44400
filename = "path_of_file.wav"


def convert_to_bin(command):
    return ''.join(format(ord(i), '08b') for i in command)


def get_encoding_duration(bin):
    return (len(bin) * 0.5) * 2


def record(seconds):
    pa = pyaudio.PyAudio()

    stream = pa.open(format=sample_format, channels=chanels, rate=smpl_rt, input=True, frames_per_buffer=chunk)

    print('Recording for {0} seconds...'.format(seconds))
    # Initialize array that be used for storing frames
    frames = []
    # Store data in chunks for 8 seconds
    for i in range(0, int(smpl_rt / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate - PortAudio interface
    pa.terminate()

    print('Done !!! ')

    # Save the recorded data in a .wav format
    sf = wave.open(filename, 'wb')
    sf.setnchannels(chanels)
    sf.setsampwidth(pa.get_sample_size(sample_format))
    sf.setframerate(smpl_rt)
    sf.writeframes(b''.join(frames))
    sf.close()


def encode(bin):
    encode_duration = get_encoding_duration(bin)
    seconds_elapsed = 0
    print('Encoding will take {0}'.format(encode_duration))
    _thread.start_new_thread(record, ((encode_duration + gen.get_tail_length() - 2), ))
    gen.head()
    for char in bin:
        seconds_elapsed = seconds_elapsed + 1
        print('Seconds reminding: {0}/{1} seconds'.format(seconds_elapsed, encode_duration))
        gen.drop()
        if char == "1":
            gen.one()
        elif char == "0":
            gen.zero()

    # Trailing pulse denotes the end of the program also gives just enough time that the recorder can stop recording
    gen.tail()


def main():
    encode(convert_to_bin(input("Input ")))


if __name__ == "__main__":
    main()
