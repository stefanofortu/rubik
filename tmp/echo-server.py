#!/usr/bin/env python3

import socket
import json
HOST = '10.42.46.45'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def doSomethingWithData(data):
    print("SERVER " + data.decode())

def getResponseToClient():
    a = {'f1': "hello", 'f2': 10, 'f3': [2, 3]}
    return json.dumps(a).encode()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    s.settimeout(1.0)
    connection = None
    try:
        while True:
            try:
                connection, addr = s.accept()
                data = connection.recv(1024)
                if not data:
                    break
                doSomethingWithData(data)
                data = getResponseToClient()
                connection.sendall(data)
            except socket.timeout:
                pass
    except KeyboardInterrupt:
        if connection:
            connection.close()
exit()