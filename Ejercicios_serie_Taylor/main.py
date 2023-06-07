import threading as t
import math as m
import time


def taylor_swift(termino, x):
    global lista_swift
    time.sleep(0.01)
    with lock:
        lista_swift.append(((-1)**termino)/(m.factorial(2*termino+1)) * x**(float(2*termino + 1)))


def suma_swift():
    global lista_swift
    global sumatoria
    sumatoria = 0
    for i in lista_swift:
        sumatoria += i


if __name__ == '__main__':
    lista_swift = []
    sumatoria = 0
    lock = t.Lock()
    terminos = int(input("Ingrese la cantidad de terminos: "))
    valor_x = float(input("Ingrese el valor de x: "))
    referencia = float(m.sin(valor_x))
    start = time.time()
    hilos = []

    for termino in range(terminos):
        th = t.Thread(target=taylor_swift, args=(termino, valor_x))
        hilos.append(th)
        th.start()
    end = time.time()

    for th in hilos:
        th.join()

    th2 = t.Thread(target=suma_swift)
    th2.start()
    th2.join()
    print(f"Tiempo de ejecucion: {end - start}")
    print("---------------------------------")
    print(f"Cantidad de terminos: {terminos}")
    print(f"Valor del seno(x): {sumatoria}")
    print(f"Valor de referencia: {referencia}")
    print(f"El error es: {abs(referencia - sumatoria)}")
