import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
# setmode imposta il metodo di riferimento ai pin.
# Se le si passa il valore GPIO.BOARD si indica 
# che si vuole accedere ai pin attraverso il loro numero,
# mentre se le si passa GPIO.BCM si indica che si utilizzera'
# il numero di porta GPIO 
# (che ricordo essere differente in alcuni casi 
# se la scheda e' di vecchio tipo).

def motorTest(motorPins):
  GPIO.setmode(GPIO.BCM)
  for pin in motorPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)


  seq = [[1,0,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,1],
         [0,0,0,1],
         [1,0,0,1]]

  #print len(seq)
  #print len(seq[0])


  #for i in range(512):
  #str1=""
  #for halfstep in range(8):
  #  for pin in range(4):
  #    str1 = str1 + str( motorPins[pin] ) +"-"+  str( seq[halfstep][pin] )

  for ripet in range(0,500):
    for halfstep in seq:
      for index,pin in enumerate(motorPins):
        GPIO.output(pin, halfstep[index])
        time.sleep(0.00025)


  #if str1 == str2:
  #  print "the same"
  GPIO.cleanup()


   #first motor in 
 # 14 15 18 GND 23

 #second motor in 
 # 14 15 18 GND 23

# Define GPIO signals to use
 #17,27,22,15
#ControlPin = [17,27,22,15]
#ControlPin = [5,6,13,19]
#ControlPin = [22,10,9,11]

motorTest([22,10,9,11]);
motorTest([5,6,13,19]);