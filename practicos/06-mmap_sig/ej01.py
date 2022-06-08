import getopt
import sys
import os
import mmap
import signal

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:')
    if len(opt) != 1:
        print("Ingrese bien la cantidad de argumentos: ")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()


for (opt,arg) in opt:
    if opt == '-f':
       path = str(arg)

memory = mmap.mmap(-1, 100)

def handler_father(s, f):
    global advance
    if s == signal.SIGUSR1:
        line = memory.readline()
        print(f"Padre acaba de recibir desde H1: {line.decode()}")
        os.kill(pidh2, signal.SIGUSR1)
    if s == signal.SIGUSR2:
        print("Padre avisa a H2 que tiene que terminar")
        advance = False
        os.kill(pidh2, signal.SIGUSR2)

def handler_h2(s, f):
    if s == signal.SIGUSR1:
        line = memory.readline()
        print(f"H2 acaba de recibir señal del padre, lee linea para guardarla en el archivo: {line.decode()}")
        with open(path, 'a') as file:
            file.write(line.decode())
            file.flush()
    if s == signal.SIGUSR2:
        print("H2 termino y avisa a padre")
        os._exit(0)

pidh1 = os.fork()
if pidh1 == 0:
    print(f"H1 pid es: {pidh1} y ppid es: {os.getppid()}\n")
    for line in sys.stdin:
        if line == 'bye\n':
            print("H1 termino y aviso a padre")
            os.kill(os.getppid(), signal.SIGUSR2)
            os._exit(0)
        else:
            print(f"H1 acaba de recibir la linea: {line}")
            memory.write(line.encode('ascii'))
            os.kill(os.getppid(), signal.SIGUSR1)

pidh2 = os.fork()
if pidh2 == 0:
    print(f"H2 pid es: {pidh2} y ppdid es: {os.getppid()}\n")
    signal.signal(signal.SIGUSR1, handler_h2)
    signal.signal(signal.SIGUSR2, handler_h2)
    while True:
        signal.pause()


advance = True
print(f"Padre pid es: {os.getpid()}\n")
signal.signal(signal.SIGUSR1, handler_father)
signal.signal(signal.SIGUSR2, handler_father)
while advance:
    signal.pause()
else:
    for i in range(2):
        os.wait()
    print("Padre espero y ahora termina")