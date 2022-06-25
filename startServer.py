import socket

from Classes.MotorHandlerServer import MotorHandlerServer


def main():
    MotorHandlerServer(simulateMotors=True)


if __name__ == "__main__":
    main()