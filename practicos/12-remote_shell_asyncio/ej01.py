import datetime, getopt, socket, sys, asyncio

async def main():
    (opt, args) = getopt.getopt(sys.argv[1:], "1:")
    try:
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    except socket.error:
        print("Error de conexion")
        sys.exit()
    print("----------Comando prompt----------")
    comand = ""

    while comand != 'exit':
        comand = input("Comando: ")
        msg = comand
        writer.write(msg.encode('ascii'))
        await writer.drain()
        data = await reader.read(10)
        print(f'Recibido: {data.decode()!r}')
        await writer.wait_closed()

        for (opt, args) in opt:
            if opt == '-1':
                file_path = args
                file = open(str(file_path), 'a')
                datetime_today = datetime.datetime.today()
                file.writelines("\n" + str(datetime_today) + "\n" + msg.decode('ascii'))
                file.close()
    exit()

asyncio.run(main())