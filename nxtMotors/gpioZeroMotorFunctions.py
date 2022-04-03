#import RPi.RPIO as RPIO
#import RPIO
import gpiozero
import time
import sys
import faulthandler
from gpiozero import DigitalInputDevice
from gpiozero import Motor

statusInput1 = ""
statusInput2 = ""
turnCounter = 0


class ArmMotor:
    def __init__(self):
        super().__init__()
    
    def __del__(self):
        pass


Mot1_Enable_Pin = 8
Mot2_Enable_Pin = 29
Mot1_PWM_Pin = 12
Mot2_PWM_Pin = 33
Mot1_Inv_Pin = 10
Mot2_Inv_Pin = 31
Mot1_decoderIN1_Pin = 16
Mot2_decoderIN1_Pin = 35
Mot1_decoderIN2_Pin = 18
Mot2_decoderIN2_Pin = 37



class NxtBaseMotor:
    def __init__(self):

        super().__init__()
        self.turnCounter=0
        
        pin_dg1="BOARD"+str(16)#Mot1_decoderIN1_Pin)
        print("pin_dg1 : ",pin_dg1)
        self.dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
        self.dg1.when_activated = self.encreaseCounter
        self.dg1.when_deactivated = self.encreaseCounter
            
        pin_dg2="BOARD"+str(18)#Mot1_decoderIN2_Pin)
        print("pin_dg2 : ",pin_dg2)
        self.dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
        self.dg2.when_activated = self.encreaseCounter
        self.dg2.when_deactivated = self.encreaseCounter
    
    
        pin_en="BOARD"+str(Mot1_Enable_Pin)
        #print("pin_en : ",pin_en)
        pin_in="BOARD"+str(Mot1_Inv_Pin)
        #print("pin_in : ",pin_in)
        #print("BOARD"+str(Mot1_Enable_Pin))
        #print("BOARD"+str(Mot1_PWM_Pin))
        pin_pwm="BOARD"+str(Mot1_PWM_Pin)
        #print("pin_pwm : ",pin_pwm)
        self.base_motor = Motor(pin_pwm, pin_in, pin_en, pwm=True)
        
        self.motorTest()
        self.small_run()
        
    def encreaseCounter(self):
        self.turnCounter+=1
    
    def printTurnCounter(self):
        print("turnCounter : ", self.turnCounter)

    def motorTest(self):
        self.base_motor.forward(speed=0.8)
        time.sleep(1)
        self.base_motor.backward(speed=0.8)
        time.sleep(1)
        self.base_motor.forward()
        self.base_motor.stop()

    def small_run(self):

        print("------------>Test1<-------------")
        self.motorTest()
        print("------------>Test-None<-------------")
        self.dg1.when_activated = None
        self.dg1.when_deactivated = None
        self.dg2.when_activated = None
        self.dg2.when_deactivated = None
        self.motorTest()
        #dg1.close()
        #dg2.close()
        #del dg1, dg2
        print("------------>Test1.1<-------------")
        #try:
        #    dg3 = DigitalInputDevice(pin_dg1,pull_up=False)
        #except:
        #    print("Error catched")
        #dg4 = DigitalInputDevice(pin_dg2,pull_up=False)
        self.dg1.when_activated = my_callback_one
        self.dg1.when_deactivated = None
        self.dg2.when_activated = my_callback_one
        self.dg2.when_deactivated = None
        self.motorTest()
            #del dg3, dg4
        print("------------>Test1.2<-------------")
        #dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
        #dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
        self.dg1.when_activated = None
        self.dg1.when_deactivated = my_callback_one
        self.dg2.when_activated = None
        self.dg2.when_deactivated = my_callback_one
        self.motorTest()
        #del dg1, dg2
        print("------------>Test1.3<-------------")
        #dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
        #dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
        self.dg1.when_activated = my_callback_one
        self.dg1.when_deactivated = my_callback_one
        self.dg2.when_activated = None
        self.dg2.when_deactivated = None
        self.motorTest()
        #del dg1, dg2
        print("------------>Test1.4<-------------")
        #dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
        #dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
        self.dg1.when_activated = None
        self.dg1.when_deactivated = None
        self.dg2.when_activated = my_callback_one
        self.dg2.when_deactivated = my_callback_one
        self.motorTest()
        #del dg1, dg2   
    
    
    def __del__(self): 
        print("going to destroy the motor object")
        time.sleep(2)
        print("now")
        self.dg1.close()
        self.dg2.close()
        #self.base_motor.close()


def my_callback_one():
    # global statusInput1 
    # statusInput1 += "|"
    global turnCounter
    turnCounter += 1


def my_callback_two():
    # global statusInput2 
    # statusInput2 += "|"
    global turnCounter
    turnCounter += 1

def startMotor(motor):
    global turnCounter
    turnCounter = 0
    motor.forward(speed=0.2)
    time.sleep(1)
    motor.backward(speed=0.2)
    time.sleep(1)
    motor.stop()
    print("turnCounter : ", turnCounter)

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
    faulthandler.enable()


    pin_dg1="BOARD"+str(Mot1_decoderIN1_Pin)
    print("pin_dg1 : ",pin_dg1)
    dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
    dg1.when_activated = my_callback_one
    dg1.when_deactivated = my_callback_one
   
    pin_dg2="BOARD"+str(Mot1_decoderIN2_Pin)
    print("pin_dg2 : ",pin_dg2)
    dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
    dg2.when_activated = my_callback_one
    dg2.when_deactivated = my_callback_one
    
    from gpiozero import Motor
    pin_en="BOARD"+str(Mot1_Enable_Pin)
    #print("pin_en : ",pin_en)
    pin_in="BOARD"+str(Mot1_Inv_Pin)
    #print("pin_in : ",pin_in)
    #print("BOARD"+str(Mot1_Enable_Pin))
    #print("BOARD"+str(Mot1_PWM_Pin))
    pin_pwm="BOARD"+str(Mot1_PWM_Pin)
    #print("pin_pwm : ",pin_pwm)
    motor = Motor(pin_pwm, pin_in, pin_en, pwm=True)
    print("------------>Test1<-------------")
    startMotor(motor)
    print("------------>Test-None<-------------")
    dg1.when_activated = None
    dg1.when_deactivated = None
    dg2.when_activated = None
    dg2.when_deactivated = None
    startMotor(motor)
    #dg1.close()
    #dg2.close()
    #del dg1, dg2
    print("------------>Test1.1<-------------")
    #try:
    #    dg3 = DigitalInputDevice(pin_dg1,pull_up=False)
    #except:
    #    print("Error catched")
    #dg4 = DigitalInputDevice(pin_dg2,pull_up=False)
    dg1.when_activated = my_callback_one
    dg1.when_deactivated = None
    dg2.when_activated = my_callback_one
    dg2.when_deactivated = None
    startMotor(motor)
        #del dg3, dg4
    print("------------>Test1.2<-------------")
    #dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
    #dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
    dg1.when_activated = None
    dg1.when_deactivated = my_callback_one
    dg2.when_activated = None
    dg2.when_deactivated = my_callback_one
    startMotor(motor)
    #del dg1, dg2
    print("------------>Test1.3<-------------")
    #dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
    #dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
    dg1.when_activated = my_callback_one
    dg1.when_deactivated = my_callback_one
    dg2.when_activated = None
    dg2.when_deactivated = None
    startMotor(motor)
    #del dg1, dg2
    print("------------>Test1.4<-------------")
    #dg1 = DigitalInputDevice(pin_dg1,pull_up=False)
    #dg2 = DigitalInputDevice(pin_dg2,pull_up=False)
    dg1.when_activated = None
    dg1.when_deactivated = None
    dg2.when_activated = my_callback_one
    dg2.when_deactivated = my_callback_one
    startMotor(motor)
    #del dg1, dg2

    dg1.close()
    dg2.close()

    return

def oldfunction():
    pin_en="BOARD"+str(Mot2_Enable_Pin)
    #print("pin en : ",pin_en) #equivalente al GPIO5
    pin_inv="BOARD"+str(Mot2_Inv_Pin)
    #print("pin  in: ",pin_inv) #equivalente al GPIO6
    pin_pwm="BOARD"+str(Mot2_PWM_Pin)
    #print("pin pwm : ",pin_pwm) #equivalente al GPIO13
    #motor2 = Motor(forward=pin_en, backward=pin_inv, enable=pin_pwm,pwm=True)

    pin_fw="GPIO6"#"BOARD"+str(Mot2_Enable_Pin)
    #print("pin fw : ",pin_fw) #equivalente al GPIO5
    pin_bw="GPIO5"#"BOARD"+str(Mot2_Inv_Pin)
    #print("pin_bw : ",pin_bw) #equivalente al GPIO6
    pin_wm_en="GPIO0"#"BOARD"+str(Mot2_PWM_Pin)
    #print("pin_wm_en : ",pin_wm_en) #equivalente al GPIO13
    
    motor2 = Motor(forward=pin_fw, backward=pin_bw, enable=pin_wm_en,pwm=True)
    
    print("forward")
    motor2.forward(speed=0.2)
    time.sleep(2)
    print("backward")
    motor2.backward(speed=0.2)
    time.sleep(2)  
    motor2.stop()
    time.sleep(2) 
    sys.exit()
    
    

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
    #RPIO.cleanup()


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
