#import RPi.RPIO as RPIO
import RPIO
import time
import sys
import faulthandler

statusInput1 = ""
statusInput2 = ""
turnCounter = 0


# migliorare funzione rendendola per singolo motore e poi richiamandola due volte
def GPIOinitialization(Mot1_Enable_Pin, Mot1_PWM_Pin, Mot1_Inv_Pin,
                       Mot2_Enable_Pin, Mot2_PWM_Pin, Mot2_Inv_Pin,
                       Mot1_decoderIN1_Pin, Mot1_decoderIN2_Pin,
                       Mot2_decoderIN1_Pin, Mot2_decoderIN2_Pin):
    # There are two ways of numbering the IO pins on a Raspberry Pi within RPi.RPIO. 
    # The first is using the BOARD numbering system.
    # This refers to the pin numbers on the P1 header of the Raspberry Pi board.
    # The advantage of using this numbering system is that your hardware will always work, 
    # regardless of the board revision of the RPi. You will not need to rewire your connector or change your code.
   
    RPIO.cleanup()
    RPIO.setmode(RPIO.BOARD)
    # setup e start value dell'enable
    print(Mot1_Enable_Pin)
    RPIO.setup(Mot1_Enable_Pin, RPIO.OUT)
    RPIO.output(Mot1_Enable_Pin, RPIO.LOW)
    print(Mot2_Enable_Pin)
    RPIO.setup(Mot2_Enable_Pin, RPIO.OUT)
    RPIO.output(Mot2_Enable_Pin, RPIO.LOW)

    # setup del bit di PWM
    RPIO.setup(Mot1_PWM_Pin, RPIO.OUT)
    RPIO.output(Mot1_PWM_Pin, RPIO.LOW)

    RPIO.setup(Mot2_PWM_Pin, RPIO.OUT)
    RPIO.output(Mot2_PWM_Pin, RPIO.LOW)

    # setup del bit di inversionePWM
    RPIO.setup(Mot1_Inv_Pin, RPIO.OUT)
    RPIO.output(Mot1_Inv_Pin, RPIO.LOW)

    RPIO.setup(Mot2_Inv_Pin, RPIO.OUT)
    RPIO.output(Mot2_Inv_Pin, RPIO.LOW)

    # setup dei pin di input del decoder, come ingressi. Per ora non setto i pullup/pullDown 
    RPIO.setup(Mot1_decoderIN1_Pin, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
    RPIO.setup(Mot2_decoderIN1_Pin, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)

    # decoder input 2
    RPIO.setup(Mot1_decoderIN2_Pin, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
    RPIO.setup(Mot2_decoderIN2_Pin, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)


def GPIOcleanup():
    print("waiting to stop Motors before exit")
    time.sleep(1)
    RPIO.cleanup()


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
    p = RPIO.PWM(Mot1_PWM_Pin, frequency_Hz)
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
    faulthandler.enable()
    try:
        # tTest : tempo di mantentimento di un valore di duty cycle --> NON USATO
        dutyCycle = 30
        if direction == 1:
            RPIO.output(PWMPin, RPIO.LOW)
            RPIO.output(InvPin, RPIO.LOW)
            # duty cycle iniziale
            dutyCycle_Init = dutyCycle  # 20
        elif direction == -1:
            RPIO.output(PWMPin, RPIO.HIGH)
            RPIO.output(InvPin, RPIO.HIGH)
            # duty cycle iniziale
            dutyCycle_Init = 100 - dutyCycle  # 80
        else:
            print("direction not valid")

        # frequenza del PWM
        frequency_Hz = 100
        # PWM setup
        p = RPIO.PWM(PWMPin, frequency_Hz)
        cnt = 0;
        global turnCounter
        turnCounter = 0

        try:
            print("duty cycle: " + str(dutyCycle_Init))  # + " for " + str(tTest) + " s")
            print("rotationSteps: " + str(rotationSteps))  # + " for " + str(tTest) + " s")
            time.sleep(0)  # wait 100ms per inizializzazione encoder
            
            # global statusInput1
            # global statusInput2
            RPIO.add_event_detect(input1, RPIO.BOTH, callback=my_callback_one)
            print("trying to avoid seg fault - removed one of the callback")
            #RPIO.add_event_detect(input2, RPIO.BOTH, callback=my_callback_two)

            p.start(dutyCycle_Init)
            time.sleep(0.1)
            RPIO.output(enablePin, RPIO.HIGH)
            lastPrint = -1
            timestamp_control = time.time()
            while turnCounter < rotationSteps:
                if turnCounter % 10  == 0 and turnCounter !=lastPrint:
                    timestamp_now = time.time()
                    print("turnCounter %d, time: %d", turnCounter, (timestamp_now-timestamp_control)*1000)       
                    timestamp_control = time.time()
                    lastPrint = turnCounter
        except KeyboardInterrupt:
            p.stop()
            if direction == +1:
                RPIO.output(PWMPin, RPIO.LOW)
            else:
                RPIO.output(PWMPin, RPIO.HIGH)
            RPIO.cleanup()
        RPIO.output(enablePin, RPIO.LOW)
        p.stop()
        
        RPIO.output(PWMPin, RPIO.LOW)
        RPIO.output(InvPin, RPIO.LOW)

        # if angle > 0:
        #    RPIO.output(PWMPin, RPIO.LOW)
        #    RPIO.output(InvPin, RPIO.LOW)
        # else:
        #    RPIO.output(PWMPin, RPIO.HIGH)
        #    RPIO.output(InvPin, RPIO.HIGH)

        RPIO.remove_event_detect(input1)
        RPIO.remove_event_detect(input2)
        time.sleep(0.1)
        # print(statusInput1)
        # print(statusInput2)
        print("turnCounter : " + str(turnCounter))
    except ValueError:
        print("Value Error --> should not happen")
    except:
        print("Able to catch seg error")
    else:
        print("There were no errors.")
    finally:
        print("Process completed.")
    faulthandler.disable()
