from Classes.MotorHandlerServer import MotorHandlerServer
import socket
import json

class MotorHandlerClient():
    def __init__(self):
        super().__init__()
        self.host = '192.168.1.136'  # Standard loopback interface address (localhost)
        self.port = 65432  # Port to listen on (non-privileged ports are > 1023)

        #self.motor_handler_server = MotorHandlerServer(simulated=True)

    def executeMovement(self, movement):
        #self.motor_handler_server.executeMovement(movement)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.host, self.port))
                b = json.dumps(movement).encode()
                s.sendall(b)
                data = s.recv(1024)
                rx = json.loads(data)
                print('Received', repr(rx))
            except ConnectionRefusedError:
                print("Server not available")