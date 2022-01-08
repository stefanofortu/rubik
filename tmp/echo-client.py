#!/usr/bin/env python3

import socket
import json

HOST = '10.42.46.45'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

a = {'field1': "hello there", 'field2': 10, 'field3': [2, 3]}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        b = json.dumps(a).encode()
        s.sendall(b)
        #s.sendall(b'Hello, world')
        data = s.recv(1024)
        print('Received', repr(data))
    except ConnectionRefusedError:
       print("Server not available")

