import codecs, multiprocessing as mp, sys

def target_h1(conn, queue):
    """Este va a leer el stdin y guardarlo en la tuberia, despues esperara recibir mediante la cola de mensajes de nuevo la linea encriptada para mostrarla por pantalla"""
    sys.stdin = open(0)
    line = sys.stdin.readline()
    conn.send(line)
    line_queue = queue.get()
    print(f'H1 recupera la linea encriptada desde la cola de mensajes: ({line_queue[:-1]})')

def target_h2(conn, queue):
    """Este va a obtener la linea desde el mp.PIPE, la encriptara y la guardara en la cola de mensajes"""
    line = conn.recv()
    line_rot13 = codecs.encode(line, 'rot_13')
    print(f'H2 ingresa la stdin ({line[:-1]}) encriptada con rot13 ({line_rot13[:-1]}) a la cola de mensajes')
    queue.put(line_rot13)

def main():
    queue = mp.Queue() # creo que la cola de mensajes
    h1_conn, h2_conn = mp.Pipe() # creo la tuberia
    h1 = mp.Process(target=target_h1, args=(h1_conn, queue))
    h2 = mp.Process(target=target_h2, args=(h2_conn, queue))

    h1.start()
    h2.start()

    h1.join()
    h2.join()

if __name__ == '__main__':
    main()