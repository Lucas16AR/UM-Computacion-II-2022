import asyncio, subprocess

async def srv(reader, writer):
    addr = writer.get_extra_info("Por nombre")
    print(f"Cliente Conectado: %s" % addr)
    data = await reader.read(10)
    message = data.decode("ascii")
    if data.decode("ascii") == "exit":
        writer.write("Terminado".encode("ascii"))
        writer.close()
    print("Direccion: %s" % str(addr))
    print("Recibido: " + data.encode("ascii"))

    result = subprocess.Popen([data], shell = True, stdout = subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = result.communicate()
    if stdout != "":
        message = "Exito\n" + stdout
    elif stderr != "":
        message = "Error\n" + stderr
        writer.write(message.encode("ascii"))
    await writer.drain()

async def main():
    server = await asyncio.start_server(
        srv, '127.0.0.1', port=8888)
    addr = server.sockets[0].getsockname()
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    print("------------Servidor Escuchando------------")
    asyncio.run(main())