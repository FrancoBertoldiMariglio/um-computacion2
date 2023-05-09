
from hashlib import sha256
import json
import random
from multiprocessing import Process, Pipe
import signal
import os

processes = []

def f():
    print("kaboom")

for i in range(10):
        process = Process(target=f, args=())
        processes.append(process)
        process.start()

for process in processes:
      print(process.pid)
      process.join()



# matriz1 = [[1, 2],
#            [3, 4]]

# matriz2 = [[5, 8],
#            [1, 9]]

# row1 = 0
# col2 = 1
# lista = []

# for i in range(4):

#     if i >= 2:
#         row1 = 1
#     lista.append(str({int(str(row1+1) + str(col2)): 
#                         (matriz1[row1][0]*matriz2[0][col2-1]) + (matriz1[row1][1]*matriz2[1][col2-1])}) + "\n")
#     col2 = (col2 % 2) + 1

# print(lista)