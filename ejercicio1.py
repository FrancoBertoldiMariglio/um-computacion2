import argparse

def numImpar():
    parser = argparse.ArgumentParser()
    parser.add_argument("entero", help="numero entero", type=int)
    args = parser.parse_args()
    cant = args.entero
    nroImpar = 1
    listaImpar = []
    if cant >= 0:
        for i in range(0, cant):
            listaImpar.append(nroImpar)
            nroImpar += 2
        print(listaImpar)
    else:
        print("Ingrese un valor valido")
    

if __name__ == '__main__':
    numImpar()