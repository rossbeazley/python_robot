__author__ = 'rdlb'

# read whiskers
# if left and right
#   back off and turn right 90
# else if left
#   back off and turn right 45
# else if right
#   back off and turn left 45
# else
#   go forwards

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(15,GPIO.IN)
GPIO.setup(4,GPIO.IN)
GPIO.setup(14,GPIO.IN)
GPIO.setup(23,GPIO.IN)

StepPinsLeft = [17,18,22,27]

for pin in StepPinsLeft:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

StepPinsRight = [9,25,11,8]

for pin in StepPinsRight:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

class Whiskers:
    def __init__(self,left,right):
        self.left = left
        self.right = right

def read_whiskers():
    return Whiskers(GPIO.input(15) or GPIO.input(23), GPIO.input(14) or GPIO.input(4))

StepCount = 4
Seq = []
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [0,1,0,0]
Seq[2] = [0,0,1,0]
Seq[3] = [0,0,0,1]

def stepForwards(StepPins):
    iteration = range(0, 4)
    step(StepPins,iteration)

def stepBackwards(StepPins):
    iteration = reversed(range(0, 4))
    step(StepPins, iteration)

def step(StepPins, iteration):
    WaitTime = 0.01
    # loop from 0 to StepCount
    for StepCounter in range(0, StepCount):
        for pin in iteration:
            xpin = StepPins[pin]
            if Seq[StepCounter][pin] != 0:
                #print " Step %i Enable %i" %(StepCounter,xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        time.sleep(WaitTime)




def back_off():
    print "BACKOFF"
    for StepCounter in range(0, 500):
        stepBackwards(StepPinsLeft)
        stepBackwards(StepPinsRight)

def right45():
    print "RIGHT 45"
    for StepCounter in range(0, 100):
        stepForwards(StepPinsRight)

def left45():
    print "LEFT 45"
    for StepCounter in range(0, 100):
        stepForwards(StepPinsLeft)

def right90():
    print "RIGHT 90"
    right45()
    right45()
    return

def forwards():
    print "FORWARDS"
    for StepCounter in range(0, 100):
        stepForwards(StepPinsLeft)
        stepForwards(StepPinsRight)


# read whiskers
# if left and right
#   back off and turn right 90
# else if left
#   back off and turn right 45
# else if right
#   back off and turn left 45
# else
#   go forwards
while True:
    whiskers = read_whiskers()
    if whiskers.left and whiskers.right:
        back_off()
        right90()
    elif whiskers.left:
        back_off()
        right45()
    elif whiskers.right:
        back_off()
        left45()
    else:
        forwards()

