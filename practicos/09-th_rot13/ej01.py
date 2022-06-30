import threading as th , codecs, sys, os

def read(w):
    print("Ingrese una oracion por favor: ")
    line = sys.stdin.readline()
    os.write(w, line.encode("ascii"))

def write(r):
    line = os.read(r, 100).decode()
    line_encode = codecs.encode(line, 'rot_13')
    print(f'Texto cifrado: {line_encode}')

if __name__ == '__main__':
    r, w = os.pipe()
    th1 = th.Thread(target = read, args = (w,))
    th2 = th.Thread(target = write, args = (r,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()