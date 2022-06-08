import codecs, multiprocessing as mp, sys

def t_h1(conn, queue):
    sys.stdin = open(0)
    line = sys.stdin.readline()
    conn.send(line)
    line_queue = queue.get()
    print(f'H1 recupera linea encriptada desde la cola de mensajes: ({line_queue[:-1]})')

def t_h2(conn, queue):
    line = conn.recv()
    line_rot13 = codecs.encode(line, 'rot_13')
    print(f'H2 ingresa la stdin ({line[:-1]}) encriptada con rot13 ({line_rot13[:-1]}) a la cola de mensajes')
    queue.put(line_rot13)

def write(name: str):
    fd = open(str(name), "w+")
    return fd

def main():
    queue = mp.Queue()
    h1_conn, h2_conn = mp.Pipe()
    h1 = mp.Process(target=t_h1, args=(h1_conn, queue))
    h2 = mp.Process(target=t_h2, args=(h2_conn, queue))

    h1.start()
    h2.start()

    h1.join()
    h2.join()

if __name__ == '__main__':
    main()