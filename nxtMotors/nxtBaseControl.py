import RPi.GPIO as GPIO
import time
import sys

turnCounter = 0

def callbackInputDecoderPin1(channel):
    global turnCounter
    turnCounter += 1

def callbackInputDecoderPin2(channel):
    global turnCounter
    turnCounter += 1

# questa funzione e' puramente di test:
# setto il motore a dutyCycle fisso per 1s
def testInputMotor(angle, direction, PWMPin, input1, input2):
    global turnCounter
    turnCounter = 0
    # duty cycle iniziale
    dutyCycle_Init=20
    # frequenza del PWM
    frequency_Hz=100

    if direction == 1:
        GPIO.output(PWMPin, GPIO.LOW)
        GPIO.output(InvPin, GPIO.LOW)
        # duty cycle iniziale
        dutyCycle_Init=20
    elif direction == -1:
        GPIO.output(PWMPin, GPIO.HIGH)
        GPIO.output(InvPin, GPIO.HIGH)
        # duty cycle iniziale
        dutyCycle_Init=80
    else:
        print("direction not valid")

    # PWM setup
    p = GPIO.PWM(PWMPin, frequency_Hz)
    p.start(dutyCycle_Init)
    try:
        # print("duty cycle: " + str(dutyCycle_Init) )
        time.sleep(0) #wait 100ms per inizializzazione encoder
        GPIO.add_event_detect(input1, GPIO.BOTH, callback = callbackInputDecoderPin1)
        GPIO.add_event_detect(input2, GPIO.BOTH, callback = callbackInputDecoderPin2)
        if angle == 90:
            ## senza ruota grande
            # rotationSteps = 800
            rotationSteps = 475
        elif angle == 180:
            ## senza ruota grande
            # rotationSteps = 250
            rotationSteps = 1020
        elif angle == 270:
            ## senza ruota grande
            # rotationSteps = 430
            rotationSteps = 1560
        elif angle == 360:
            ## senza ruota grande
            # rotationSteps = ( 600 + 10)
            rotationSteps = 2100
        elif angle == 5:
            ## inteso come piccolo aggiustamento manuale
            rotationSteps = 2
        else:
            print("Input not valid")
            rotationSteps=0

        while turnCounter < rotationSteps:
            pass
            time.sleep(0)
    except KeyboardInterrupt:
        pass

    p.stop()
    GPIO.output(PWMPin, GPIO.LOW)
    GPIO.remove_event_detect(input1)
    GPIO.remove_event_detect(input2)
    time.sleep(0.001)
    #print("turnCounter : " + str(turnCounter))


# There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. 
# The first is using the BOARD numbering system.
# This refers to the pin numbers on the P1 header of the Raspberry Pi board.
# The advantage of using this numbering system is that your hardware will always work, 
# regardless of the board revision of the RPi. You will not need to rewire your connector or change your code.

###########################################################################
# Vedi .nxtTest.py per la spiegazione e il funzionamento di quanto settato sotto
#
GPIO.setmode(GPIO.BOARD)
# Utilizzo il pin 29 del GPIO per abilitazione del motore.
Mot1_Enable_Pin=29
# Il PIN 33 è PWM1: GPIO con la capacità di fare PWM
Mot1_PWM_Pin=33
# Il PIN 31 e' l'altro filo che pilota il motore. Il motore DC lavora per differenza tra Mot1_PWM_Pin e Mot1_Inv_Pin;
Mot1_Inv_Pin=31
# decoder input 1
Mot1_decoderIN1_Pin = 35
# decoder input 2
Mot1_decoderIN2_Pin = 37

# setup e start value dell'enable
GPIO.setup(Mot1_Enable_Pin, GPIO.OUT)
GPIO.output(Mot1_Enable_Pin, GPIO.HIGH)

# setup del bit di PWM
GPIO.setup(Mot1_PWM_Pin, GPIO.OUT)
GPIO.output(Mot1_PWM_Pin, GPIO.LOW)

# setup del bit di inversionePWM
GPIO.setup(Mot1_Inv_Pin, GPIO.OUT)
GPIO.output(Mot1_Inv_Pin, GPIO.LOW)

# setup dei pin di input del decoder, come ingressi. Per ora non setto i pullup/pullDown 
GPIO.setup(Mot1_decoderIN1_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# decoder input 2
GPIO.setup(Mot1_decoderIN2_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

###########################################################################

inUnser = "L"
while inUnser.lower() != "q":
    inUnser = str(input("What you want to do?[r]:rotate,\n[1]:90,[2]:180,[3]:270,[4]:360,[5]:+10,[Q]:Quit : "))
    if inUnser == "1" :
        testInputMotor(angle=90, PWMPin=Mot1_PWM_Pin, input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
        time.sleep(1)
    elif inUnser.lower() == "2":
        testInputMotor(angle=180, PWMPin=Mot1_PWM_Pin, input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
        time.sleep(1)
    elif inUnser.lower() == "3":
        testInputMotor(angle=270,PWMPin=Mot1_PWM_Pin, input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif inUnser.lower() == "4":
        testInputMotor(angle=360,PWMPin=Mot1_PWM_Pin, input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif inUnser.lower() == "5":
        testInputMotor(angle=5,  PWMPin=Mot1_PWM_Pin, input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)
    elif inUnser.lower() == "q":
        pass
    else:
        print("Choice not valid. Try again")

# funzione di test del PWM

# Need to stop for 1s in order to stop Motors before exit")
time.sleep(1)

GPIO.cleanup()

print("Program ended")
exit()