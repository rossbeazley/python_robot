__author__ = 'rdlb'
import unittest
import Motors


class FakeOutPin:
    def __init__(self):
        self.levels = []

    def high(self):
        self.levels.append(True)

    def low(self):
        self.levels.append(False)


class Movement(unittest.TestCase):
    def setUp(self):
        self.pin1 = FakeOutPin()
        self.pin2 = FakeOutPin()
        self.pin3 = FakeOutPin()
        self.pin4 = FakeOutPin()
        self.pins = [self.pin1, self.pin2, self.pin3, self.pin4]
        self.stepper = Motors.StepperMotor(self.pins)

    def test_forwards_pin1(self):
        self.stepper.stepForwards()
        self.assertListEqual(self.pin1.levels, [True, False, False, False])

    def test_forwards_pin2(self):
        self.stepper.stepForwards()
        self.assertListEqual(self.pin2.levels, [False, True, False, False])

    def test_forwards_pin3(self):
        self.stepper.stepForwards()
        self.assertListEqual(self.pin3.levels, [False, False, True, False])

    def test_forwards_pin4(self):
        self.stepper.stepForwards()
        self.assertListEqual(self.pin4.levels, [False, False, False, True])

    def test_backwards_pin4(self):
        self.stepper.stepBackwards()
        self.assertListEqual(self.pin4.levels, [True, False, False, False])

    def test_backwards_pin3(self):
        self.stepper.stepBackwards()
        self.assertListEqual(self.pin3.levels, [False, True, False, False])

    def test_backwards_pin2(self):
        self.stepper.stepBackwards()
        self.assertListEqual(self.pin2.levels, [False, False, True, False])

    def test_backwards_pin1(self):
        self.stepper.stepBackwards()
        self.assertListEqual(self.pin1.levels, [False, False, False, True])
