## Ejercicio del TP3 - Uso de Fork() - SUMA DE PROCESOS PARES

# Fork es un metodo de python que sirve para crear procesos hijos de otros.

#----------------------------------#

import argparse
from curses.ascii import EM
from multiprocessing.connection import wait
import os
from queue import Empty
import subprocess
from time import sleep
import time
from tokenize import group


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help="Numero de Forks a realizar (n de proc hijos). EJ: '3'")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-he', action='store_true', help="Activa: Ayuda.")
    group.add_argument('-v', action='store_true', help="Activa: Modo Verboso.")
    args = parser.parse_args()

    if args.he:
        print("AYUDA: \n")
        help_F(args)
    else:
        print("Ejecutado SIN ayuda.\n")

    if args.n and args.v:
        print("Ejecucion CON Modo Verboso\n")
        verbose(args)
    elif args.n:
        fork_F(args)
    else:
        print("Ejecucion SIN Modo Verboso\n")


def fork_F(args):        
    for i in range(args.n):
        ret = os.fork()
        if ret == 0:
            # print(subprocess.check_output(["ps", "fax"], universal_newlines=True))
            suma = 0
            i = 0
            while i <= os.getpid():
                if i % 2 == 0:
                    suma = suma+i
                i+=1
            print("PID: ", os.getpid(), "-", "PPID: ", os.getppid(), ":", suma)
            # time.sleep(2)
            os._exit(0)
        else:
            time.sleep(0.0001)
            os.wait()


def verbose(args):
    STARTING = "Starting process"
    ENDING = "Ending process"
    

    for i in range(args.n):
        ret = os.fork()
        # for i in range(0, args.n):
        if ret == 0:
            print(STARTING, os.getpid())
            # print(subprocess.check_output(["ps", "fax"], universal_newlines=True))
            suma = 0
            i = 0
            while i <= os.getpid():
                if i % 2 == 0:
                    suma = suma+i
                i+=1
            print(ENDING, os.getpid())
            print("PID: ", os.getpid(), "-", "PPID: ", os.getppid(), ":", suma)
            os._exit(0)
            # time.sleep(2)
        else:
            time.sleep(0.01)
            os.wait()


def help_F(args):
    INIT_TXT= """Como usar:
                            1. Escriba en su terminal 'python3'.
                            2. Seguido de '-n' donde debe poner la cantidad de procesos hijos a crear.
                            3. Luego puede elegir si agregar el Modo Verboso, escribiendo '-v', el cual mostrará detalles
                            sobre como se va ejecutando el proceso.
                            4. Por ultimo de 'Enter' para comenzar la ejecucion.
                            """
    print(INIT_TXT)


if __name__=='__main__':
    main()

#
#