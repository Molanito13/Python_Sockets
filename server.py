# echo-server.py

import socket
import ahorcado
import requests

HOST = "10.112.0.219"  # Standard loopback interface address (localhost)
PORT = 65430  # Port to listen on (non-privileged ports are > 1023)

response = requests.get("https://palabras-aleatorias-public-api.herokuapp.com/random")

palabra = response.json()["body"]["Word"].upper()
vidas = 6

l1 = [i for i in palabra]
l2 = ["_" for i in palabra]
letras = []
flag = False
print(l1)
print(l2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))

    while(True):
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:

                flag = False
                print(l2)
                data = conn.recv(1024)
                    
                if not data:
                    break
                data.decode('utf-8')

                letra = data.decode().upper()

                if data.decode().upper() not in letras:

                    letras.append(letra)

                    for i in range(0,len(l1)):
                        if letra == l1[i]:
                                l2[i] = letra
                                flag = True
                    
                    if flag == False:
                        vidas -= 1
                else:
                    vidas -= 1
                
                if l1 == l2 or vidas == 0:
                    aux = "".join(l2)
                    data = (ahorcado.stages[vidas] + "\n"+ aux + ";").encode()
                    conn.sendall(data)
                    break

                
                aux = "".join(l2)
                data = (ahorcado.stages[vidas] + "\n"+ aux).encode()

                

                conn.sendall(data)

        s.shutdown(socket.SHUT_RDWR)
        s.close()
        
        print(l2)
        break

                