__author__ = 'rdlb'
import time


class StepperMotor:
    StepCount = 4
    Seq = []
    Seq = range(0, StepCount)
    Seq[0] = [1, 0, 0, 0]
    Seq[1] = [0, 1, 0, 0]
    Seq[2] = [0, 0, 1, 0]
    Seq[3] = [0, 0, 0, 1]

    def __init__(self, pins):
        self.StepPins = pins

    def stepForwards(self):
        iteration = range(0, self.StepCount)
        self._step(iteration)

    def stepBackwards(self):
        iteration = [3, 2, 1, 0]
        self._step(iteration)

    def _step(self, iteration):
        WaitTime = 0.01
        # loop from 0 to StepCount
        for StepCounter in iteration:
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin] != 0:
                    xpin.high()
                else:
                    xpin.low()
            time.sleep(WaitTime)


class MotorControl:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def back_off(self):
        print "BACKOFF"
        for StepCounter in range(0, 100):
            self.left.stepBackwards()
            self.right.stepBackwards()

    def left45(self):
        print "RIGHT 45"
        for StepCounter in range(0, 600):
            self.right.stepForwards()
            self.left.stepBackwards()

    def right45(self):
        print "LEFT 45"
        for StepCounter in range(0, 600):
            self.left.stepForwards()
            self.right.stepBackwards()

    def right90(self):
        print "RIGHT 90"
        self.right45()
        self.right45()
        return

    def forwards(self):
        print "FORWARDS"
        for StepCounter in range(0, 100):
            self.left.stepForwards()
            self.right.stepForwards()
