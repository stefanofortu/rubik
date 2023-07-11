#import RPi.GPIO as GPIO
import time
import sys

statusInput1 = ""
statusInput2 = ""
turnCounter = 0


# migliorare funzione rendendola per singolo motore e poi richiamandola due volte
def GPIOinitialization(Mot1_Enable_Pin, Mot1_PWM_Pin, Mot1_Inv_Pin,
                       Mot2_Enable_Pin, Mot2_PWM_Pin, Mot2_Inv_Pin,
                       Mot1_decoderIN1_Pin, Mot1_decoderIN2_Pin,
                       Mot2_decoderIN1_Pin, Mot2_decoderIN2_Pin):
    # There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. 
    # The first is using the BOARD numbering system.
    # This refers to the pin numbers on the P1 header of the Raspberry Pi board.
    # The advantage of using this numbering system is that your hardware will always work, 
    # regardless of the board revision of the RPi. You will not need to rewire your connector or change your code.
    GPIO.setmode(GPIO.BOARD)

    # setup e start value dell'enable
    GPIO.setup(Mot1_Enable_Pin, GPIO.OUT)
    GPIO.output(Mot1_Enable_Pin, GPIO.LOW)

    GPIO.setup(Mot2_Enable_Pin, GPIO.OUT)
    GPIO.output(Mot2_Enable_Pin, GPIO.LOW)

    # setup del bit di PWM
    GPIO.setup(Mot1_PWM_Pin, GPIO.OUT)
    GPIO.output(Mot1_PWM_Pin, GPIO.LOW)

    GPIO.setup(Mot2_PWM_Pin, GPIO.OUT)
    GPIO.output(Mot2_PWM_Pin, GPIO.LOW)

    # setup del bit di inversionePWM
    GPIO.setup(Mot1_Inv_Pin, GPIO.OUT)
    GPIO.output(Mot1_Inv_Pin, GPIO.LOW)

    GPIO.setup(Mot2_Inv_Pin, GPIO.OUT)
    GPIO.output(Mot2_Inv_Pin, GPIO.LOW)

    # setup dei pin di input del decoder, come ingressi. Per ora non setto i pullup/pullDown 
    GPIO.setup(Mot1_decoderIN1_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Mot2_decoderIN1_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # decoder input 2
    GPIO.setup(Mot1_decoderIN2_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Mot2_decoderIN2_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def GPIOcleanup():
    print("waiting to stop Motors before exit")
    time.sleep(1)
    GPIO.cleanup()


# questa funzione e' puramente di test:
# ogni tTest cambio il duty cycle da 0 a 100 e poi di nuovo a 0
def testDutyCycle(Mot1_PWM_Pin):
    # tempo di mantentimento di un valore di duty cycle
    tTest = 0.5
    # duty cycle iniziale
    dutyCycle_Init = 0
    # frequenza del PWM
    frequency_Hz = 100
    # intervallo di tempo tra un cambio di Dc e l'altro
    # PWM setup
    p = GPIO.PWM(Mot1_PWM_Pin, frequency_Hz)
    p.start(dutyCycle_Init)
    try:
        for dc in range(0, 101, 25):
            print("duty cycle: " + str(dc))
            p.ChangeDutyCycle(dc)
            time.sleep(tTest)
        for dc in range(100, -1, -25):
            print("duty cycle: " + str(dc))
            p.ChangeDutyCycle(dc)
            time.sleep(tTest)
    except KeyboardInterrupt:
        pass
    p.stop()


def my_callback_one(channel):
    # global statusInput1 
    # statusInput1 += "|"
    global turnCounter
    turnCounter += 1


def my_callback_two(channel):
    # global statusInput2 
    # statusInput2 += "|"
    global turnCounter
    turnCounter += 1


def nxtMotorRotation(tTest, direction, rotationSteps, PWMPin, InvPin, enablePin, input1, input2):
    # tTest : tempo di mantentimento di un valore di duty cycle --> NON USATO
    dutyCycle = 30
    if direction == 1:
        GPIO.output(PWMPin, GPIO.LOW)
        GPIO.output(InvPin, GPIO.LOW)
        # duty cycle iniziale
        dutyCycle_Init = dutyCycle  # 20
    elif direction == -1:
        GPIO.output(PWMPin, GPIO.HIGH)
        GPIO.output(InvPin, GPIO.HIGH)
        # duty cycle iniziale
        dutyCycle_Init = 100 - dutyCycle  # 80
    else:
        print("direction not valid")

    # frequenza del PWM
    frequency_Hz = 100
    # PWM setup
    p = GPIO.PWM(PWMPin, frequency_Hz)
    cnt = 0;
    global turnCounter
    turnCounter = 0

    try:
        print("duty cycle: " + str(dutyCycle_Init))  # + " for " + str(tTest) + " s")
        print("rotationSteps: " + str(rotationSteps))  # + " for " + str(tTest) + " s")
        time.sleep(0)  # wait 100ms per inizializzazione encoder
        
        # global statusInput1
        # global statusInput2
        GPIO.add_event_detect(input1, GPIO.BOTH, callback=my_callback_one)
        GPIO.add_event_detect(input2, GPIO.BOTH, callback=my_callback_two)

        p.start(dutyCycle_Init)
        time.sleep(0.1)
        GPIO.output(enablePin, GPIO.HIGH)
        lastPrint = -1
        while turnCounter < rotationSteps:
            if turnCounter % 10  == 0 and turnCounter !=lastPrint:
                print(turnCounter)
                lastPrint = turnCounter
            time.sleep(0)
    except KeyboardInterrupt:
        p.stop()
        if direction == +1:
            GPIO.output(PWMPin, GPIO.LOW)
        else:
            GPIO.output(PWMPin, GPIO.HIGH)
        GPIO.cleanup()
    GPIO.output(enablePin, GPIO.LOW)
    p.stop()
    
    GPIO.output(PWMPin, GPIO.LOW)
    GPIO.output(InvPin, GPIO.LOW)

    # if angle > 0:
    #    GPIO.output(PWMPin, GPIO.LOW)
    #    GPIO.output(InvPin, GPIO.LOW)
    # else:
    #    GPIO.output(PWMPin, GPIO.HIGH)
    #    GPIO.output(InvPin, GPIO.HIGH)

    GPIO.remove_event_detect(input1)
    GPIO.remove_event_detect(input2)
    time.sleep(0.1)
    # print(statusInput1)
    # print(statusInput2)
    print("turnCounter : " + str(turnCounter))
