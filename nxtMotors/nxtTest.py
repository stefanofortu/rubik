import RPi.GPIO as GPIO
import time
#GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
#GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

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