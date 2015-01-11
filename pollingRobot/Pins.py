__author__ = 'rdlb'
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class In:
    def __init__(self, pinId):
        self.pinId = pinId
        GPIO.setup(pinId, GPIO.IN)

    def read(self):
        return GPIO.input(self.pinId)


class Out:
    def __init__(self, pinId):
        self.pinId = pinId
        GPIO.setup(pinId, GPIO.OUT)
        GPIO.output(pinId, False)

    def high(self):
        GPIO.output(self.pinId, True)

    def low(self):
        GPIO.output(self.pinId, False)
