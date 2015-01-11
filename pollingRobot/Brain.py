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
class Simple:
    def __init__(self, motors, whiskers):
        self.motors = motors
        self.whiskers = whiskers

    def _actOn(self, state):
        if state.left and state.right:
            self.motors.back_off()
            self.motors.right90()
        elif state.left:
            self.motors.back_off()
            self.motors.right45()
        elif state.right:
            self.motors.back_off()
            self.motors.left45()
        else:
            self.motors.forwards()

    def run(self):
        while True:
            state = self.whiskers.read_whiskers()
            self._actOn(state)

