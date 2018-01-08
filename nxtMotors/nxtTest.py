import RPi.GPIO as GPIO
import time
import sys

# There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. 
# The first is using the BOARD numbering system.
# This refers to the pin numbers on the P1 header of the Raspberry Pi board.
# The advantage of using this numbering system is that your hardware will always work, 
# regardless of the board revision of the RPi. You will not need to rewire your connector or change your code.
#

Motor1Pin1    = 24
Motor1Pin2    = 26

Encoder1Pin1  = 16
Encoder1Pin2  = 18

GPIO.setmode(GPIO.BOARD)

def forwardMotor1(x):
    GPIO.output(Motor1Pin1, GPIO.HIGH)
    print("forwarding running motor")
    time.sleep(x)
    GPIO.output(Motor1Pin1, GPIO.LOW)

def reverseMotor1(x):
    GPIO.output(Motor1Pin2, GPIO.HIGH)
    print("backwarding running motor")
    time.sleep(x)
    GPIO.output(Motor1Pin2, GPIO.LOW)

edgeTimeOld=0

def encoderRising(channel):
    global edgeTimeOld
    if channel==Encoder1Pin1:
        pass
        #print('Encoder 1 Rising')
    elif channel==Encoder1Pin2:
        pass
        #print('Encoder 2 Rising')
    else:
        print("Channel not correct")

    edgeTimeNow = time.time()
    pulseTime   = edgeTimeNow - edgeTimeOld
    print("edgeTime {:.3f} ms".format(pulseTime*1000))
    edgeTimeOld = edgeTimeNow

def forwardMotor1Shafts(shafts):
    i=0
    GPIO.output(Motor1Pin1, GPIO.HIGH)
    print("forwarding running motor")
    while( i < shafts ):
        GPIO.wait_for_edge(Encoder1Pin1, GPIO.RISING)
        i+=1;
    GPIO.output(Motor1Pin1, GPIO.LOW)

    GPIO.output(Motor1Pin2, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(Motor1Pin2, GPIO.LOW)


timeSleep=2

try:   
    GPIO.setup(Motor1Pin1, GPIO.OUT)
    GPIO.setup(Motor1Pin2, GPIO.OUT)
    GPIO.output(Motor1Pin1, GPIO.LOW)
    GPIO.output(Motor1Pin2, GPIO.LOW)

    GPIO.setup(Encoder1Pin1, GPIO.IN)
    GPIO.setup(Encoder1Pin2, GPIO.IN)
    
    if GPIO.input(Encoder1Pin1):
        print('Input was HIGH')
    else:
        print('Input was LOW')
    if GPIO.input(Encoder1Pin2):
        print('Input was HIGH')
    else:
        print('Input was LOW')

    #GPIO.add_event_detect(Encoder1Pin1, GPIO.RISING, callback=encoderRising)  # add rising edge detection on a channel
    #GPIO.add_event_detect(Encoder1Pin2, GPIO.RISING, callback=encoderRising)  # add rising edge detection on a channel

    forwardMotor1Shafts(25)
    '''
    forwardMotor1(timeSleep)
    time.sleep(timeSleep)
    reverseMotor1(timeSleep)
    '''
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print("exiting....\n") # print value of counter

except:
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!", sys.exc_info()[0])
finally:
    '''
    GPIO CLEANUP : http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi
    '''
    print("\nProgram end")
    GPIO.cleanup() # this ensures a clean exit 


exit()
























#DA QUA IN POI, PWM
#p = GPIO.PWM(12, 0.5)

FREQUENCY_HZ = 100  # Hertz
DUTY_CYCLE   = 50   # duty cycle (0.0 <= duty cycle <= 100.0)
SLEEP_TIME   = 1

GPIO.setup(33, GPIO.OUT)
'''
p = GPIO.PWM(33, FREQUENCY_HZ)
p.start(DUTY_CYCLE)
#input('Press return to stop:')   # use raw_input for Python 2
time.sleep(10)
p.stop()
GPIO.cleanup()
'''

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

p = GPIO.PWM(12, 1)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()

#p.start(1)
for i in range(10):
    GPIO.output(29, GPIO.HIGH)
    #GPIO.output(33, GPIO.HIGH)
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(37, GPIO.HIGH)
    time.sleep(0.125)
    GPIO.output(29, GPIO.LOW)
    #GPIO.output(33, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    time.sleep(0.125)
#p.stop()
GPIO.cleanup()