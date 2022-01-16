from Classes.MotorHandlerServer import MotorHandlerServer

class MotorHandlerClient():
    def __init__(self):
        super().__init__()
        self.host = '10.42.46.45'  # Standard loopback interface address (localhost)
        self.port = 65432  # Port to listen on (non-privileged ports are > 1023)

        self.motor_handler_server = MotorHandlerServer()

    def executeMovement(self, movement):
        self.motor_handler_server.executeMovement(movement)


