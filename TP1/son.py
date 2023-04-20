import os


class son():

    def aLaburarMijo(self, fdIn, fdOut):
        line = ""
        try:
            while True:
                char = os.read(fdIn, 1)
                if str(char) == str(b'\n'):
                    break
                line += str(char.decode())
            lineReverse = line[::-1].replace("'", "")
            esc = bytes(lineReverse + "\n", 'utf-8')
            os.write(fdOut, esc)
        except:
            print("El pipe esta vacio, soy un hijo")
