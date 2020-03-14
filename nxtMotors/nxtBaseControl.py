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
def testInputMotor(angle, PWMPin, input1, input2):
    # duty cycle iniziale
    dutyCycle_Init=20
    # frequenza del PWM
    frequency_Hz=100
    # PWM setup
    p = GPIO.PWM(PWMPin, frequency_Hz)
    p.start(dutyCycle_Init)
    try:
        # print("duty cycle: " + str(dutyCycle_Init) )
        time.sleep(0) #wait 100ms per inizializzazione encoder
        GPIO.add_event_detect(input1, GPIO.BOTH, callback = callbackInputDecoderPin1)
        GPIO.add_event_detect(input2, GPIO.BOTH, callback = callbackInputDecoderPin2)
        if angle == 90:
            rotationSteps = 800
        elif angle == 180:
            rotationSteps = 250
        elif angle == 270:
            rotationSteps = 430
        elif angle == 360:
            rotationSteps = ( 600 + 10)
        else:
            print("Input not valid")
            rotationSteps=0
        global turnCounter
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

# funzione di test del PWM
testInputMotor(angle=360,PWMPin=Mot1_PWM_Pin, input1=Mot1_decoderIN1_Pin,input2=Mot1_decoderIN2_Pin)


# Need to stop for 1s in order to stop Motors before exit")
time.sleep(1)

GPIO.cleanup()

exit()