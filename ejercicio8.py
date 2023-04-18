import os
import time


def pipeClose():
    os.pipe()
    rt = os.fork()

    if rt > 0:
        print(os.getpid())
        exit()

    elif rt == 0:
        print(os.getpid())
        time.sleep(100)
        print("hola")

if __name__ == '__main__':
    pipeClose()
