import os
import time
from multiprocessing import current_process

class son():

    def invert(self, fdIn, fdOut, length):
        try:
            line = os.read(fdIn, length)
            lineReverse = line[::-1]
            os.write(fdOut, lineReverse)
            # processName = current_process.name
            # print(f"Nombre proceso: {processName}")
            time.sleep(2)
        except:
            print("El pipe esta vacio, soy hijo")

    # def invert2(self, fdIn, fdOut):
    #     line = ""
    #     try:
    #         while True:
    #             char = os.read(fdIn, 1)
    #             if str(char) == str(b'\n'):
    #                 break
    #             line += str(char.decode())
    #         lineReverse = line[::-1].replace("'", "")
    #         esc = bytes(lineReverse + "\n", 'utf-8')
    #         os.write(fdOut, esc)
    #     except:
    #         print("El pipe esta vacio, soy un hijo")
