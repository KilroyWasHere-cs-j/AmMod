import numpy as np

import functionGenerator as gen


def convert_to_bin(command):
    return ''.join(format(ord(i), '08b') for i in command)


def encode(bin):
    for char in bin:
        print(char)
        if char == "1":
            gen.dit()
        elif char == "0":
            gen.dah()


def main():
    encode(convert_to_bin(input("Input ")))


if __name__ == "__main__":
    main()
