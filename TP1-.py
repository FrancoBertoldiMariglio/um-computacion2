import os
import time


def txt(path):

    pipe1 = "/tmp/pIn"
    if not os.path.exists(pipe1):
        os.mkfifo(pipe1)
    pipe2 = "/tmp/pOut"
    if not os.path.exists(pipe2):
        os.mkfifo(pipe2)
    input = open(path, "r")
    file = input.readlines()
    for line in file:
        pipeIn = os.fdopen(os.open(pipe1, os.O_RDWR), "w")
        pipeIn.write(line)
        pipeIn.flush()
        rt = os.fork()
        if rt > 0:
            time.sleep(3)
        if rt == 0: 
            pipeIn = os.fdopen(os.open(pipe1, os.O_RDWR), "r")
            line = pipeIn.read()
            lineReverse = line[::-1]
            pipeOut = os.fdopen(os.open(pipe2, os.O_RDWR), "w")
            pipeOut.write(lineReverse)
            pipeOut.flush()
            exit()

    pipeOutFd = os.fdopen(os.open(pipe2, os.O_RDWR), "r")
    file1 = pipeOutFd.read()
    print(file1)
    # file = line.readlines()
    # list = [i.strip("\n") for i in file]
    # for i in list:
    #     print(i)
    # if len(line) == 0:
    #     break


if __name__ == '__main__':
    txt("/home/franco/Escritorio/um-computacion2/prueba")
