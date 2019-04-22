import RPi.GPIO as GPIO
import time
import sys

# questa funzione è puramente di test:
# ogni tTest cambio il duty cycle da 0 a 100 e poi di nuovo a 0
def testDutyCycle(Mot1_PWM_Pin):
    # tempo di mantentimento di un valore di duty cycle
    tTest = 0.1
    # duty cycle iniziale
    dutyCycle_Init=0
    # frequenza del PWM
    frequency_Hz=100
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

# There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. 
# The first is using the BOARD numbering system.
# This refers to the pin numbers on the P1 header of the Raspberry Pi board.
# The advantage of using this numbering system is that your hardware will always work, 
# regardless of the board revision of the RPi. You will not need to rewire your connector or change your code.
GPIO.setmode(GPIO.BOARD)
# Pin 29 --> enable
# Pin 31 --> PWM
# Pin 33 --> inversione per PWM (2)
# Pin 35 --> input1 encoder
# Pin 36 --> input2 encoder

# References
# [1] : NXT: http://trivox.tripod.com/lego-nxt-motor-input-output.html
# [2] : L298N : https://tronixlabs.com.au/news/tutorial-l298n-dual-motor-controller-module-2a-and-arduino/

# Utilizzo il pin 29 del GPIO per abilitazione del motore.
# Se enable = 1(5V) --> motore abilitato.
# Se outputMot1_Enable = 0 (0V) --> motore non abilitato.
# questo va collegato al pin 7 del L298N [2]. Il pin a cui va collegato è quello più esterno. Quello interno è fisso a 5V
Mot1_Enable_Pin=29

# Il PIN 33 è PWM1: GPIO con la capacità di fare PWM
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_PWM_Pin=33

# Il PIN 31 e' l'altro filo che pilota il motore. Il motore DC lavora per differenza tra Mot1_PWM_Pin e Mot1_Inv_Pin;
# se Mot1_Inv_Pin=0 allora il segnale che pilota motore è PWM
# se Mot1_Inv_Pin=0 allora il segnale che pilota direttamente il motore è invertito
# questo va collegato al pin 8 o 9 del L298N [2](dipende dal verso di rotazione che si vuole dare)
# LN298 lo amplifica e lo porta in uscita al bianco/nero del NXT
Mot1_Inv_Pin=31

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
# 5           yellow  rotation detector output 1 --> collegato al pin 35/36 encoder
# 6           blue    rotation detector output 2 --> collegato al pin 35/36 encoder


# setup e start value dell'enable
GPIO.setup(Mot1_Enable_Pin, GPIO.OUT)
GPIO.output(Mot1_Enable_Pin, GPIO.HIGH)

# setup del bit di PWM
GPIO.setup(Mot1_PWM_Pin, GPIO.OUT)

# setup del bit di inversionePWM
GPIO.setup(Mot1_Inv_Pin, GPIO.OUT)
GPIO.output(Mot1_Inv_Pin, GPIO.LOW)

# funzione di test del PWM
# testDutyCycle(Mot1_PWM_Pin)

GPIO.cleanup()

exit()

#Motor1Pin1    = 24
#Motor1Pin2    = 26

#Encoder1Pin1  = 16
#Encoder1Pin2  = 18
# def forwardMotor1(x):
#     GPIO.output(Motor1Pin1, GPIO.HIGH)
#     print("forwarding running motor")
#     time.sleep(x)
#     GPIO.output(Motor1Pin1, GPIO.LOW)

# def reverseMotor1(x):
#     GPIO.output(Motor1Pin2, GPIO.HIGH)
#     print("backwarding running motor")
#     time.sleep(x)
#     GPIO.output(Motor1Pin2, GPIO.LOW)

# edgeTimeOld=0

# def encoderRising(channel):
#     global edgeTimeOld
#     if channel==Encoder1Pin1:
#         pass
#         #print('Encoder 1 Rising')
#     elif channel==Encoder1Pin2:
#         pass
#         #print('Encoder 2 Rising')
#     else:
#         print("Channel not correct")

#     edgeTimeNow = time.time()
#     pulseTime   = edgeTimeNow - edgeTimeOld
#     print("edgeTime {:.3f} ms".format(pulseTime*1000))
#     edgeTimeOld = edgeTimeNow

# def forwardMotor1Shafts(shafts):
#     i=0
#     GPIO.output(Motor1Pin1, GPIO.HIGH)
#     print("forwarding running motor")
#     while( i < shafts ):
#         GPIO.wait_for_edge(Encoder1Pin1, GPIO.RISING)
#         i+=1;
#     GPIO.output(Motor1Pin1, GPIO.LOW)

#     GPIO.output(Motor1Pin2, GPIO.HIGH)
#     time.sleep(0.001)
#     GPIO.output(Motor1Pin2, GPIO.LOW)


# timeSleep=2

# try:   
#     GPIO.setup(Motor1Pin1, GPIO.OUT)
#     GPIO.setup(Motor1Pin2, GPIO.OUT)
#     GPIO.output(Motor1Pin1, GPIO.LOW)
#     GPIO.output(Motor1Pin2, GPIO.LOW)

#     GPIO.setup(Encoder1Pin1, GPIO.IN)
#     GPIO.setup(Encoder1Pin2, GPIO.IN)
    
#     if GPIO.input(Encoder1Pin1):
#         print('Input was HIGH')
#     else:
#         print('Input was LOW')
#     if GPIO.input(Encoder1Pin2):
#         print('Input was HIGH')
#     else:
#         print('Input was LOW')

#     #GPIO.add_event_detect(Encoder1Pin1, GPIO.RISING, callback=encoderRising)  # add rising edge detection on a channel
#     #GPIO.add_event_detect(Encoder1Pin2, GPIO.RISING, callback=encoderRising)  # add rising edge detection on a channel

#     forwardMotor1Shafts(25)
#     '''
#     forwardMotor1(timeSleep)
#     time.sleep(timeSleep)
#     reverseMotor1(timeSleep)
#     '''
# except KeyboardInterrupt:  
#     # here you put any code you want to run before the program   
#     # exits when you press CTRL+C  
#     print("exiting....\n") # print value of counter

# except:
#     # this catches ALL other exceptions including errors.  
#     # You won't get any error messages for debugging  
#     # so only use it once your code is working  
#     print("Other error or exception occurred!", sys.exc_info()[0])
# finally:
#     '''
#     GPIO CLEANUP : http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi
#     '''
#     print("\nProgram end")
#     GPIO.cleanup() # this ensures a clean exit 


#exit()

#BLUE =  31
#WHITE = 33

#GPIO.setup(BLUE, GPIO.OUT)
#GPIO.setup(WHITE , GPIO.OUT)

#GPIO.output(BLUE, GPIO.HIGH)
#GPIO.output(WHITE, GPIO.LOW)

#time.sleep(0.2)
#print("5s")

#GPIO.output(BLUE, GPIO.LOW)
#GPIO.output(WHITE, GPIO.HIGH)

#time.sleep(2)
#GPIO.cleanup()
#exit()

#DA QUA IN POI, PWM

outputMot1_Enable=29
outputMot1=33
outputMot2=31

#p = GPIO.PWM(outputMot1, 0.5)

FREQUENCY_HZ = 100  # Hertz
DUTY_CYCLE   = 30   # duty cycle (0.0 <= duty cycle <= 100.0)
SLEEP_TIME   = 1

GPIO.setup(outputMot1, GPIO.OUT)
GPIO.setup(outputMot2, GPIO.OUT)
GPIO.setup(outputMot1_Enable, GPIO.OUT)

GPIO.output(outputMot2, GPIO.LOW)
GPIO.output(outputMot1_Enable, GPIO.HIGH)

p = GPIO.PWM(outputMot1, FREQUENCY_HZ)
p.start(DUTY_CYCLE)
#a=input('Press return to stop:')   # use raw_input for Python 2
time.sleep(2)
p.stop()
GPIO.cleanup()


exit()


p = GPIO.PWM(33, FREQUENCY_HZ)
p.start(DUTY_CYCLE)
for dc in range(0, 101, 25):
    p.ChangeDutyCycle(dc)
    time.sleep(SLEEP_TIME)
    print(dc)
for dc in range(100, -1, -25):
    p.ChangeDutyCycle(dc)
    print(dc)
    time.sleep(SLEEP_TIME)
p.stop()
GPIO.cleanup()



exit()


