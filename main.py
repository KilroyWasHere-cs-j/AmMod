import sys


def main(args):
    mode = args[1]
    if mode == "M":
        text = args[2]
        print(text)
    elif mode == "D":
        #  demod
        pass



if __name__ == "__main__":
    main(sys.argv)
