from nxtMotors.nxtMotorFunctions import GPIOcleanup, GPIOinitialization,nxtMotorRotation
import time
# References
# [1] : NXT: http://trivox.tripod.com/lego-nxt-motor-input-output.html
# [2] : L298N : https://tronixlabs.com.au/news/tutorial-l298n-dual-motor-controller-module-2a-and-arduino/
# Utilizzo il pin 29 del GPIO per abilitazione del motore.
# Se enable = 1(5V) --> motore abilitato.
# Se outputMot1_Enable = 0 (0V) --> motore non abilitato.
# questo va collegato al pin 7 del L298N [2]. Il pin a cui va collegato è quello più esterno. Quello interno è fisso a 5V
Mot1_Enable_Pin = 29
Mot2_Enable_Pin = 8
# Il PIN 33 è PWM1: GPIO con la capacità di fare PWM
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_PWM_Pin = 33
Mot2_PWM_Pin = 12
# Il PIN 31 e' l'altro filo che pilota il motore. Il motore DC lavora per differenza tra Mot1_PWM_Pin e Mot1_Inv_Pin;
# se Mot1_Inv_Pin=0 allora il segnale che pilota motore è PWM
# se Mot1_Inv_Pin=0 allora il segnale che pilota direttamente il motore è invertito
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_Inv_Pin = 31
Mot2_Inv_Pin = 10
# decoder input 1
Mot1_decoderIN1_Pin = 35
Mot2_decoderIN1_Pin = 16
# decoder input 2
Mot1_decoderIN2_Pin = 37
Mot2_decoderIN2_Pin = 18
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



class MotorHandlerServer():
    def __init__(self):
        super().__init__()
        self.host = '10.42.46.45'  # Standard loopback interface address (localhost)
        self.port = 65432  # Port to listen on (non-privileged ports are > 1023)
        self.ArmPosition = "GO" # arm position : necessary to compensate rotation during base rotation
        # Physically speaking it has no sense - encoders are related to position....Whatever...
        self.startServer()
        GPIOinitialization()

    def __del__(self):
        GPIOcleanup()

    def startServer(self):
        print("Server Up and Running")

    def executeMovement(self, movement):
        print("executeMovement")
        if not self.fromRPi:
            return
        if movement.name == "ciao" and movement.direction == 0:
            print("INIT To Be Implemented")
            exit()
            # nxtMotorRotation(1, direction=-1, rotationSteps=50,
            #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
            #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement.name == "ciao" and movement.direction == 0:
            print("GO --> START To Be Implemented")
            exit()
            # nxtMotorRotation(1, direction=-1, rotationSteps=310,
            #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
            #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement.name == "ciao" and movement.direction == 0:
            print("START --> GO To Be Implemented")
            exit()
            # nxtMotorRotation(1, direction=+1, rotationSteps=300,
            #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
            #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement.name == "ARM_goUp" and movement.direction == 0:
            nxtMotorRotation(1, direction=-1, rotationSteps=200,
                             PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                             input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement.name == "ARM_goDown" and movement.direction == 0:
            nxtMotorRotation(1, direction=+1, rotationSteps=200,
                             PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
                             input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        elif movement.name == "ARM_flipCube" and movement.direction == 0:
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
        elif movement.name == "BASE_change" and movement.direction == 90:
            nxtMotorRotation(1, direction=+1, rotationSteps=537,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            time.sleep(1)
            nxtMotorRotation(1, direction=-1, rotationSteps=12,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        elif movement.name == "BASE_change" and movement.direction == -90:
            nxtMotorRotation(1, direction=+1, rotationSteps=1020,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)

        # elif movement.name == "BASE_change" and movement.direction == +270:
        #    nxtMotorRotation(1, direction=+1, rotationSteps=1560,
        #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)

        # elif movement.name == "BASE_change" and movement.direction == +360:
        #    nxtMotorRotation(1, direction=+1, rotationSteps=2100,
        #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        elif movement.name == "BASE_change" and movement.direction == 10:
            nxtMotorRotation(1, direction=+1, rotationSteps=5,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)

        elif movement.name == "BASE_change" and movement.direction == -10:
            nxtMotorRotation(1, direction=-1, rotationSteps=5,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)

        elif movement.name == "BASE_rotation" and movement.direction == 90:
            nxtMotorRotation(1, direction=+1, rotationSteps=537,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
            time.sleep(1)
            nxtMotorRotation(1, direction=-1, rotationSteps=12,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        elif movement.name == "BASE_rotation" and movement.direction == -90:
            nxtMotorRotation(1, direction=+1, rotationSteps=1020,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        #elif movement.name == "BASE_rotation" and movement.direction == +270:
        #    nxtMotorRotation(1, direction=+1, rotationSteps=1560,
        #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        #elif movement.name == "BASE_rotation" and movement.direction == +360:
        #    nxtMotorRotation(1, direction=+1, rotationSteps=2100,
        #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        elif movement.name == "BASE_rotation" and movement.direction == 10:
            nxtMotorRotation(1, direction=+1, rotationSteps=5,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        elif movement.name == "BASE_rotation" and movement.direction == -10:
            nxtMotorRotation(1, direction=-1, rotationSteps=5,
                             PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                             input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)