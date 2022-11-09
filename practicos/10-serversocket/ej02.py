import socket, getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], "h:p:")
    if len(opt) != 2:
        print ("Ingrese bien la cantidad de argumentos...")
        exit()
except getopt.GetoptError as error:
    print (f"Error: %s" % error)
    exit()

for (op,ar) in opt:
    if op == '-h':
        host = str(ar)
    if op == '-p':
        port = int(ar)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Ingrese un comando")

while True:
    command = input("Ingrese un comando")
    s.send(command.encode())
    if command == 'exit':
        break
    result = s.recv(1024)
    print(result.decode())