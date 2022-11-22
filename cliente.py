# echo-client.py

import socket

HOST = "10.112.0.219"  # The server's hostname or IP address
PORT = 65429 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(input('HOLA INTRODUCE UN DATO: ').encode())
        data = s.recv(4096)
        # if data == "Fin".encode():
        #     print(data.decode())
        print(data.decode())

        if data.decode() [-1:] == ";":
            break