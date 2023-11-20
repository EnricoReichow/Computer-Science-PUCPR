#!/usr/bin/env python3
import socket
import sys

HOST = '127.0.0.1'  
PORT = 9988 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except:
    print('# erro de bind')
    sys.exit()

s.listen(5)
print('Aguardando conexões em', PORT)

while True:
    conn, addr = s.accept()
    print('Recebi uma conexão de', addr)

    while True:
        data = conn.recv(1024) 
        if not data:
            break 

        print('Dados recebidos:', data.decode('utf-8'))

    print('O cliente encerrou')
    conn.close()
