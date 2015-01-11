__author__ = 'rdlb'

import Pins
import Motors
import Whiskers
import Brain


StepPinsLeft = [Pins.Out(17), Pins.Out(18), Pins.Out(22), Pins.Out(27)]
left = Motors.StepperMotor(StepPinsLeft)

StepPinsRight = [Pins.Out(9), Pins.Out(25), Pins.Out(11), Pins.Out(8)]
right = Motors.StepperMotor(StepPinsRight)

motors = Motors.MotorControl(left, right)

whiskers = Whiskers.Whiskers(Pins.In(15), Pins.In(23), Pins.In(14), Pins.In(4))

brain = Brain.Simple(motors, whiskers)
brain.run()
