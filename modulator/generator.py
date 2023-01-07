from pysine import sine


# Because python is too much of a beta bitch to have structs
class pulseSettings():
    pluse_width = 0.5  # Length of pulse
    tail_length = 6  # Number of trailing pulses after message
    head_length = int(tail_length / 2)  # Number of leading pulses before message
    one_freq = 1000  # Freq for one
    zero_freq = 500  # Freq for two
    r2z_freq = zero_freq + ((one_freq - zero_freq) / 2)  # Freq for
    head_freq = r2z_freq  # Freq for head
    tail_freq = r2z_freq  # Freq for tail


def one():
    sine(pulseSettings.one_freq, pulseSettings.pluse_width)


def zero():
    sine(pulseSettings.zero_freq, pulseSettings.pluse_width)


def drop():
    sine(pulseSettings.r2z_freq, pulseSettings.pluse_width)


def tail():
    for i in range(0, pulseSettings.tail_length):
        sine(pulseSettings.tail_freq, pulseSettings.pluse_width)


def head():
    for i in range(0, pulseSettings.head_length):
        sine(pulseSettings.head_freq, pulseSettings.pluse_width)


def get_head_length():
    return pulseSettings.head_length


def get_tail_length():
    return pulseSettings.tail_length
