from nxtMotorFunctions import GPIOinitialization, GPIOcleanup, nxtMotorRotation
import time
import RPi.GPIO as GPIO

# References
# [1] : NXT: http://trivox.tripod.com/lego-nxt-motor-input-output.html
# [2] : L298N : https://tronixlabs.com.au/news/tutorial-l298n-dual-motor-controller-module-2a-and-arduino/

# Utilizzo il pin 29 del GPIO per abilitazione del motore.
# Se enable = 1(5V) --> motore abilitato.
# Se outputMot1_Enable = 0 (0V) --> motore non abilitato.
# questo va collegato al pin 7 del L298N [2]. Il pin a cui va collegato è quello più esterno. Quello interno è fisso a 5V
Mot1_Enable_Pin=29
Mot2_Enable_Pin=8
# Il PIN 33 è PWM1: GPIO con la capacità di fare PWM
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_PWM_Pin=33
Mot2_PWM_Pin=12
# Il PIN 31 e' l'altro filo che pilota il motore. Il motore DC lavora per differenza tra Mot1_PWM_Pin e Mot1_Inv_Pin;
# se Mot1_Inv_Pin=0 allora il segnale che pilota motore è PWM
# se Mot1_Inv_Pin=0 allora il segnale che pilota direttamente il motore è invertito
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_Inv_Pin=31
Mot2_Inv_Pin=10
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

GPIOinitialization(     Mot1_Enable_Pin=Mot1_Enable_Pin, Mot1_PWM_Pin=Mot1_PWM_Pin,  Mot1_Inv_Pin=Mot1_Inv_Pin,   
                        Mot2_Enable_Pin=Mot2_Enable_Pin, Mot2_PWM_Pin=Mot2_PWM_Pin,  Mot2_Inv_Pin=Mot2_Inv_Pin,   
                        Mot1_decoderIN1_Pin=Mot1_decoderIN1_Pin, Mot1_decoderIN2_Pin=Mot1_decoderIN2_Pin,
                        Mot2_decoderIN1_Pin=Mot2_decoderIN1_Pin, Mot2_decoderIN2_Pin=Mot2_decoderIN2_Pin)

userInput = ""
while userInput.lower() != "q":
    print("Select one option:")
    print("[1]:+9O(Down) [2]:+180(Down) [3]:+10(Down) [4]:-10(Down)")
    print("[7]:+9O(Up)   [8]:+180(Up)   [9]:+10(Up)   [10]:-10(Up)")  
    print("[I]nit  [S]tart  [G]o  [U]p  [D]own  [R]otate  [Q]uit")
    userInput = input("")
    if userInput.lower() == "i" : #per initialization only
        nxtMotorRotation(1, direction=-1, rotationSteps=50, 
                        PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)    

    elif userInput.lower() == "s" : #da ROTATE A START : "Start" : "S"
        nxtMotorRotation(1,direction=-1, rotationSteps=310, 
                        PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)

    if userInput.lower() == "g" : # da START A ROTATE : "Go" : "G"
        nxtMotorRotation(1, direction=+1, rotationSteps=300, 
                        PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)

    elif userInput.lower() == "u" : # from ROTATE to UP : "Up" : "U"     
        nxtMotorRotation(1, direction=-1, rotationSteps=200, 
                        PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)
    
    elif userInput.lower() == "d" : #da UP a ROTATE : "Down" : "D"
        nxtMotorRotation(1, direction=+1, rotationSteps=200, 
                        PWMPin=Mot2_PWM_Pin,InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)
    
    elif userInput.lower() == "r" : # da ROTATE A ROTATE : "Rotation" : "R"
        nxtMotorRotation(1, direction=+1, rotationSteps=150, 
                        PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)
        time.sleep(0.25)
        nxtMotorRotation(1, direction=-1, rotationSteps=300, 
                        PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)
        time.sleep(0.1)
        nxtMotorRotation(1, direction=+1, rotationSteps=125, 
                        PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin, 
                        input1=Mot2_decoderIN1_Pin,input2=Mot2_decoderIN2_Pin)
    elif userInput.lower() == "1" : # +90 degree
        nxtMotorRotation(1, direction=+1, rotationSteps=537, 
                        PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                        input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
        time.sleep(1)
        nxtMotorRotation(1,direction=-1, rotationSteps=12, 
                        PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                        input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "2": # +180 degree
        nxtMotorRotation(1,direction=+1, rotationSteps=1020, 
                        PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                        input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)

    elif userInput.lower() == "3": # +270 degree
        nxtMotorRotation(1, direction=+1, rotationSteps=1560,
                        PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                        input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "4": # +360 degree
        nxtMotorRotation(1, direction=+1, rotationSteps=2100,
                        PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                        input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "5": # +90 degree
        nxtMotorRotation(1, direction=+1, rotationSteps=5,
                        PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                        input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "6": # +90 degree
        nxtMotorRotation(1, direction=-1, rotationSteps=5,
                        PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
                        input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "q":
        pass
    else:
        print("Choice not valid. Try again")

print("waiting to stop Motors before exit")
#time.sleep(0.1)
#print("Mot1_PWM_Pin : " + str(Mot1_PWM_Pin))
#GPIO.output(Mot1_PWM_Pin, GPIO.HIGH)
time.sleep(1)
#GPIO.output(Mot1_PWM_Pin, GPIO.LOW)

GPIOcleanup()