from Classes.MotorMovement import MotorMovement
from nxtMotors.nxtMotorFunctions import nxtMotorRotation
import time
import sys

import json
import socket

# References
# [1] : NXT: http://trivox.tripod.com/lego-nxt-motor-input-output.html
# [2] : L298N : https://tronixlabs.com.au/news/tutorial-l298n-dual-motor-controller-module-2a-and-arduino/
# Utilizzo il pin 29 del GPIO per abilitazione del motore.
# Se enable = 1(5V) --> motore abilitato.
# Se outputMot1_Enable = 0 (0V) --> motore non abilitato.
# questo va collegato al pin 7 del L298N [2]. Il pin a cui va collegato è quello più esterno. Quello interno è fisso a 5V
Mot1_Enable_Pin = 8
Mot2_Enable_Pin = 29
# Il PIN 33 è PWM1: GPIO con la capacità di fare PWM
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_PWM_Pin = 12
Mot2_PWM_Pin = 33
# Il PIN 31 e' l'altro filo che pilota il motore. Il motore DC lavora per differenza tra Mot1_PWM_Pin e Mot1_Inv_Pin;
# se Mot1_Inv_Pin=0 allora il segnale che pilota motore è PWM
# se Mot1_Inv_Pin=0 allora il segnale che pilota direttamente il motore è invertito
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_Inv_Pin = 10
Mot2_Inv_Pin = 31
# decoder input 1
Mot1_decoderIN1_Pin = 16
Mot2_decoderIN1_Pin = 35
# decoder input 2
Mot1_decoderIN2_Pin = 18
Mot2_decoderIN2_Pin = 37

################################################################
# NXT - MOTOR
################################################################
# INPUT
# nxt-cable   color   signal                      polarity
# 1           white   motor power supply          DC 9V -/+     ---> collegato output L298N
# 2           black   motor power supply          DC 9V -/+     ---> collegato output L298N
# 3           red     rotation detector supply    ground (0V) DC ---> collegato massa L298N
# 4           green   rotation detector supply    + 4.3(to 5.0 V) ---> collegato 5V stabilizzati L298N
# OUTPUT
# 5           yellow  rotation detector output 1 --> collegato al pin 35 encoder
# 6           blue    rotation detector output 2 --> collegato al pin 37 encoder


class MotorHandlerServer:
    def __init__(self, simulateMotors=False, run_server_locally=False):
        super().__init__()
        self.simulateMotors = simulateMotors
        self.ArmPosition = "GO"  # arm position : necessary to compensate rotation during base rotation
        # Physically speaking it has no sense - encoders are related to position....Whatever...

        self.run_server_locally = run_server_locally
        if not self.run_server_locally:
            self.startServer()

        if not self.simulateMotors:
            from nxtMotors.nxtMotorFunctions import GPIOinitialization
            GPIOinitialization(Mot1_Enable_Pin=Mot1_Enable_Pin, 
                Mot1_PWM_Pin=Mot1_PWM_Pin, Mot1_Inv_Pin=Mot1_Inv_Pin,
                Mot2_Enable_Pin=Mot2_Enable_Pin, Mot2_PWM_Pin=Mot2_PWM_Pin, 
                Mot2_Inv_Pin=Mot2_Inv_Pin,
                Mot1_decoderIN1_Pin=Mot1_decoderIN1_Pin, Mot1_decoderIN2_Pin=Mot1_decoderIN2_Pin,
                Mot2_decoderIN1_Pin=Mot2_decoderIN1_Pin, Mot2_decoderIN2_Pin=Mot2_decoderIN2_Pin)

    def __del__(self):
        if not self.simulateMotors:
            from nxtMotors.nxtMotorFunctions import GPIOcleanup
            GPIOcleanup()

    def startServer(self):
        print("Server Up and Running")
        local_ip = socket.gethostbyname(socket.gethostname())
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((local_ip, 65432))
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
                        self.doSomethingWithData(data)
                        data = self.getResponseToClient()
                        connection.sendall(data)
                    except socket.timeout:
                        pass
            except KeyboardInterrupt:
                if connection:
                    connection.close()

    def doSomethingWithData(self, data):
        # print("SERVER received : " + data.decode())
        data_rx = json.loads(data)
        if data_rx["header"] == "ping":
            print("Ping from client received")
        elif data_rx["header"] == "movement":
            rx_movement = data_rx["data"]
            movement = MotorMovement(name=rx_movement['name'],direction=rx_movement['direction'])
            self.executeMovement(movement)
        else:
            print("Data not expected")

    def getResponseToClient(self):
        result = {'result': "OK"}
        return json.dumps(result).encode()

    def executeMovement(self, movement):
        print("executeMovement : ")
        print(movement)
        time.sleep(0.01)
        return
        print("executeMovement : ")
        print(movement)

        if movement['motor'] == "ARM" and movement['movement'] == "ARM_toward_Start" and movement['direction'] == 0:
            nxtMotorRotation(1, direction=-1, rotationSteps=50,
                                PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement['motor'] == "ARM" and movement['movement'] == "ARM_Start_To_Rotate" and movement['direction'] == 0:
            print(movement['movement'])
            nxtMotorRotation(1, direction=+1, rotationSteps=310,
                                PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement['motor'] == "ARM" and movement['movement'] == "ARM_Rotate_to_Start" and movement['direction'] == 0:
            print(movement['movement'])
            nxtMotorRotation(1, direction=-1, rotationSteps=300,
                                PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement['motor'] == "ARM" and movement['movement'] == "ARM_goUp" and movement['direction'] == 0:
            waitTimer = 0.5
        # if movement['motor'] == "ARM" and movement['movement'] == "INIT" and movement['direction'] == 0:
        if movement.name == "ciao" and movement.direction == 0:

            print("INIT To Be Implemented")
            # nxtMotorRotation(1, direction=-1, rotationSteps=50,
            #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
            #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
            #   elif movement['motor'] == "ARM" and movement['movement'] == "goStart" and movement['direction'] == 0:
        elif movement.name == "ciao" and movement.direction == 0:
            print("GO --> START To Be Implemented")
            # nxtMotorRotation(1, direction=-1, rotationSteps=310,
            #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
            #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        #elif movement['motor'] == "ARM" and movement['movement'] == "startGo" and movement['direction'] == 0:
        elif movement.name == "ciao" and movement.direction == 0:
            print("START --> GO To Be Implemented")

            # nxtMotorRotation(1, direction=+1, rotationSteps=300,
            #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
            #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement.name == "ARM_goUp" and movement.direction == 0:
        #elif movement['motor'] == "ARM" and movement['movement'] == "ARM_goUp" and movement['direction'] == 0:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=-1, rotationSteps=200,
                                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
            else:
                print("executing ARM_goUp : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "ARM_goDown" and movement.direction == 0:
        #elif movement['motor'] == "ARM" and movement['movement'] == "ARM_goDown" and movement['direction'] == 0:
            # elif movement.name == "ARM_goDown" and movement.direction == 0:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=200,
                                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
            else:
                print("executing ARM_goDown : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "ARM_flipCube" and movement.direction == 0:
        #elif movement['motor'] == "ARM" and movement['movement'] == "ARM_flipCube" and movement['direction'] == 0:
            # elif movement.name == "ARM_flipCube" and movement.direction == 0:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=150,
                                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
                time.sleep(0.25)
                nxtMotorRotation(1, direction=-1, rotationSteps=300,
                                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
                time.sleep(0.1)
                nxtMotorRotation(1, direction=+1, rotationSteps=125,
                                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
            else:
                print("executing flipCube : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "BASE_change" and movement.direction == +90:
        #elif movement['motor'] == "BASE" and movement['movement'] == "BASE_change" and movement['direction'] == +90:
            # elif movement.name == "BASE_change" and movement.direction == 90:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=537,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
                time.sleep(waitTimer)
                nxtMotorRotation(1, direction=-1, rotationSteps=12,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_change +90 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "BASE_change" and movement.direction == -90:
        #elif movement['motor'] == "BASE" and movement['movement'] == "BASE_change" and movement['direction'] == -90:
            # elif movement.name == "BASE_change" and movement.direction == -90:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=1020,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_change -90 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        # elif movement.name == "BASE_change" and movement.direction == +270:
        #    nxtMotorRotation(1, direction=+1, rotationSteps=1560,
        #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)

        # elif movement.name == "BASE_change" and movement.direction == +360:
        #    nxtMotorRotation(1, direction=+1, rotationSteps=2100,
        #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        elif movement.name == "BASE_change" and movement.direction == +10:
        # elif movement['motor'] == "BASE" and movement['movement'] == "BASE_change" and movement['direction'] == 10:
            # elif movement.name == "BASE_change" and movement.direction == 10:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=5,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_change 10 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "BASE_change" and movement.direction == -10:
        #elif movement['motor'] == "BASE" and movement['movement'] == "BASE_change" and movement['direction'] == -10:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=-1, rotationSteps=5,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_change -10 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "BASE_rotation" and movement.direction == +90:

        # elif movement['motor'] == "BASE" and movement['movement'] == "BASE_rotation" and movement['direction'] == 90:
            # elif movement.name == "BASE_rotation" and movement.direction == 90:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=537,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
                time.sleep(waitTimer)
                nxtMotorRotation(1, direction=-1, rotationSteps=12,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_rotation +90 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "BASE_rotation" and movement.direction == -90:

        # elif movement['motor'] == "BASE" and movement['movement'] == "BASE_rotation" and movement['direction'] == -90:
            # elif movement.name == "BASE_rotation" and movement.direction == -90:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=1020,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            # elif movement.name == "BASE_rotation" and movement.direction == +270:
            #    nxtMotorRotation(1, direction=+1, rotationSteps=1560,
            #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
            #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            # elif movement.name == "BASE_rotation" and movement.direction == +360:
            #    nxtMotorRotation(1, direction=+1, rotationSteps=2100,
            #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
            #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_rotation -90 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "BASE_rotation" and movement.direction == +10:

            # elif movement['motor'] == "BASE" and movement['movement'] == "BASE_rotation" and movement['direction'] == 10:
            # elif movement.name == "BASE_rotation" and movement.direction == 10:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=+1, rotationSteps=5,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_rotation 10 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        elif movement.name == "BASE_rotation" and movement.direction == -10:
            # elif movement['motor'] == "BASE" and movement['movement'] == "BASE_rotation" and movement['direction'] == -10:
            # elif movement.name == "BASE_rotation" and movement.direction == -10:
            if not self.simulateMotors:
                nxtMotorRotation(1, direction=-1, rotationSteps=5,
                                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            else:
                print("executing BASE_rotation -10 : .....", end="")
                sys.stdout.flush()
                time.sleep(waitTimer)
                print("DONE")
        else:
            print("movement not valid : ", end="")
            print(movement)
