__author__ = 'rdlb'
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class In:
    def __init__(self, pinId):
        self.pinId = pinId
        try:
            GPIO.setup(pinId, GPIO.IN)
            print "Setting in pin " + str(pinId)
        except:
            print "Error setting pin " + str(pinId)

    def read(self):
        return GPIO.input(self.pinId)


class Out:
    def __init__(self, pinId):
        self.pinId = pinId
        GPIO.setup(pinId, GPIO.OUT)
        GPIO.output(pinId, False)
        print "Setting out pin " + str(pinId)

    def high(self):
        GPIO.output(self.pinId, True)

    def low(self):
        GPIO.output(self.pinId, False)
