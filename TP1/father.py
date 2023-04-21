import os


class dad():

    def sendLines(self, fdIn, lines):

        for line in lines:
            esc = bytes(line, 'utf-8')
            os.write(fdIn, esc)

    def readLines(self, fdOut, length):

        try:
            line = os.read(fdOut, length)
            lineDecode = line.decode()
            return lineDecode
        except:
            print("El pipe esta vacio, soy el padre")

    # def readLines2(self, fdOut):

    #     line = ""
    #     try:
    #         while True:
    #             char = os.read(fdOut, 1)
    #             if len(char) == 0:
    #                 break
    #             if str(char) == str(b'\n'):
    #                 print(line)
    #                 line = ""
    #             line += str(char.decode())
    #     except:
    #         print("El pipe esta vacio, soy el padre")
