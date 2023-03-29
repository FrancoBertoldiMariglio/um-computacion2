import argparse
import os
import math as ma


def fork():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numero", help="numero al que sacarle la raiz")
    parser.add_argument("-f", "--fork", help="hace el fork del programa")
    args = parser.parse_args()

    if args.fork:
        ret = os.fork()
        if ret > 0:
            return ma.sqrt(int(args.numero))
        elif ret == 0:
            return 1/ma.sqrt(int(args.numero))
    return ma.sqrt(int(args.numero))

if __name__ == '__main__':
    print(fork())
