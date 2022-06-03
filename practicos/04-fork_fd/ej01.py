import os
import getopt
import sys
import time

'''
-n <N>
-r <R>
-h
-f <ruta_archivo>
-v
'''

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'n:f:r:v:hv')
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()


modo_verboso = False

for (opc,ar) in opt:
    if opc == '-n':
        num_hijos = int(ar)
    if opc == '-f':
        file = ar
    if opc == '-r':
        len = int(ar)
    if opc == '-h':
        print(("Ejecutar programa {ej01.py -n 5 -r 5 -f exit.txt} "))
    if opc == '-v':
        modo_verboso = True

def hijo(letra: str):
    if not os.fork():
        print("Hijo escribiendo...")

        if modo_verboso:
            print(f'Proceso: {os.getpid()} letra: {letra}')
        for i in range(len):
            fd.write(letra)
            fd.flush()
            time.sleep(1)
        print("Finalizo escritura...")
        os._exit(0)

def escribir(name: str):
    fd = open(str(name), "w+")
    return fd

def leer(name: str):
    fd = open(str(name), "r")
    lines = fd.readlines()
    print(f"Archivo: {lines[0]}")

if __name__ == '__main__':

    fd = escribir(file)
    for i in range(num_hijos):
        hijo(ABC[i])
    for i in range(num_hijos):
        os.wait()
    leer(file)