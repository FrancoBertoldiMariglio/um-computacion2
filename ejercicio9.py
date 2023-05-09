"""Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado 
en una fifo indicando el indice del elemento. El padre deberá leer en la fifo y mostrar 
el resultado final."""

import os
import math
import time
import json
import ast
import sys
import subprocess as sp


def matrix():

    pipe = "/tmp/pfifo"
    if not os.path.exists(pipe):
        os.mkfifo(pipe)
    
    matriz1 = [[1, 2],
               [3, 4]]

    matriz2 = [[5, 8],
               [1, 9]]
    
    rt = os.fork()

    if rt == 0:
        print("Hijo 1: " + str(getPid()))
        pipeout = os.open(pipe, os.O_WRONLY)
        os.write(pipeout, str(
            {11: (matriz1[0][0]*matriz2[0][0]) + (matriz1[0][1]*matriz2[1][0])}) + "\n")
        exit()

    rt = os.fork()

    if rt == 0:
        print("Hijo 2: " + str(getPid()))
        pipeout = os.open(pipe, os.O_WRONLY)
        os.write(pipeout, str(
            {12: (matriz1[0][0]*matriz2[0][1]) + (matriz1[0][1]*matriz2[1][1])}) + "\n")
        exit()

    rt = os.fork()

    if rt == 0:
        print("Hijo 3: " + str(getPid()))
        pipeout = os.open(pipe, os.O_WRONLY)
        os.write(pipeout, str(
            {21: (matriz1[1][0]*matriz2[0][0]) + (matriz1[1][1]*matriz2[1][0])}) + "\n")
        exit()

    rt = os.fork()

    if rt == 0:
        print("Hijo 4: " + str(getPid()))
        pipeout = os.open(pipe, os.O_WRONLY)
        os.write(pipeout, str(
            {22: (matriz1[1][0]*matriz2[0][1]) + (matriz1[1][1]*matriz2[1][1])}) + "\n")
        exit()

    if rt > 0:
        print(getPid())
        pipein = open(pipe, "r")
        file = pipein.readlines()
        list = [i.strip("\n") for i in file]
        listDict = [ast.literal_eval(i) for i in list]
        for i in listDict:
            print(str(i.keys()) + ": " + str(i.values()))
        p = sp.Popen(["rm", "/tmp/pfifo"])


    # row1 = 0
    # col2 = 1

    # for i in range(4):
        
    #     rt = os.fork()

    #     if rt == 0:
    #         if i >= 2:
    #             row1 = 1
    #         print(getPid())
    #         # time.sleep(1)
    #         pipeout = os.open(pipe, os.O_WRONLY)
    #         data = str({int(str(row1+1) + str(col2)): 
    #                     (matriz1[row1][0]*matriz2[0][col2-1]) + (matriz1[row1][1]*matriz2[1][col2-1])}) + "\n"
    #         os.write(pipeout, bytes(data, "utf-8"))
    #         col2 = (col2 % 2) + 1
    #         exit()



def getPid(): 
    return "PID: " + str(os.getpid()) + " PPID: " + str({os.getppid()})


if __name__ == '__main__':
    matrix()
