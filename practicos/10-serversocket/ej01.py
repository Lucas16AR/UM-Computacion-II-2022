import getopt, threading, socket, subprocess, socketserver, os, sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self, client):
        addr = client
        while True:
            data = self.request.recv(1024)
            message = data.decode("ascii")
            if data.decode('ascii') == 'exit':
                client.send('Terminado'.encode('ascii'))
                break
            print("Direccion: %s" % str(addr))
            print("Recibido:" + data.decode('ascii'))
            result = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = result.communicate()
            if stdout != "":
                message = "Ok\n" + stdout
            elif stderr != "":
                message = "Error\n" + stderr

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

def main():
    try:
        (opt, ar) = getopt.getopt(sys.argv[1:], 'm:')
    except:
        sys.exit(1)

    for (op, ar) in opt:
        if op == ['-m']:
            opt = ar
        else:
            sys.exit(2)
    address = ('localhost', 8888)
    if opt == 'p':
        server = ForkedTCPServer(address, MyTCPHandler)
        print("Servidor en bucle corriendo en proceso: ", os.getpid())
    elif opt == 'h':
        server = ThreadedTCPServer(address, MyTCPHandler)
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = ss.accept()
    th = threading.Thread(target=server.serve_forever, args=(client,))
    th.setDaemon(True)
    th.start()
    ip, port = ('localhost', 0)
    ss.connect((ip, port))
    addr = client
    
    if opt == 't':
        print("Servidor en bucle corriendo en hilo: ", th.getName())

    while True:
        msg = input("Ingrese un mensaje: ")
        ss.send(msg.encode('ascii'))
        data = ss.recv(1024).decode('ascii')
        print(data)
        if msg == 'exit':
            server.shutdown()
            ss.close()
            server.socket.close()

if __name__ == "__main__":
    main()