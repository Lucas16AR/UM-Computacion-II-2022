import sys, os, time, threading

DELAY = 10

def th_func(name):
    print("Este es el hilo: %s (%d)" % (name, threading.current_thread().name, threading.current_thread().ident))
    time.sleep(name)
    print("El hilo %d: terminando" % name)

if __name__ == "__main__":
    print("Iniciando programa principal: antes de crear el thread___ mi PID es %d (%d)" % (os.getpid(), threading.current_thread().ident))

    x1 = threading.Thread(target = th_func, args=(1,), daemon = True) 
    x2 = threading.Thread(target = th_func, args=(2,)) 
    
    x1.start()
    x2.start()
  
    print("Cantidad de threads activos: ", threading.active_count())


    for i in threading.enumerate():
        print("Nombre: ", i.name, "(",i.ident,", Vivo?: ",i.is_alive(),", Daemon?:",i.daemon)

    time.sleep(1.5)
    print("Estado x1: ", x1.is_alive())
    x1.join()