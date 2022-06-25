from Classes.MotorHandlerServer import MotorHandlerServer
import socket
import json


class MotorHandlerClient:
    def __init__(self, run_server_locally=False, server_address='192.168.1.75', simulateMotors=False):
        super().__init__()
        self.run_server_locally = run_server_locally
        self.server_address = server_address  # Standard loopback interface address (localhost)
        self.server_port = 65432  # Port to listen on (non-privileged ports are > 1023)
        self.motor_handler_server = None
        if self.run_server_locally:
            # creo una istanza del server, da richiamare direttamente
            self.motor_handler_server = MotorHandlerServer(run_server_locally=run_server_locally,
                                                           simulateMotors=simulateMotors)
        else:
            # se non faccio girare in locale, allora ci deve essere già un altro processo che attiva il server
            # controllo che sia attivo
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((self.server_address, self.server_port))
                    b = json.dumps(dict(header="ping", data="")).encode()
                    s.sendall(b)
                except ConnectionRefusedError:
                    print("Server not available")
                    exit()

    def executeMovement(self, movement):
        if self.run_server_locally:
            self.motor_handler_server.executeMovement(movement)
        else:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((self.server_address, self.server_port))
                    b = json.dumps(dict(header="movement", data=movement)).encode()
                    #b = json.dumps(movement).encode()
                    s.sendall(b)
                    data = s.recv(1024)
                    rx = json.loads(data)
                    print('Received', repr(rx))
                except ConnectionRefusedError:
                    print("Server not available")
