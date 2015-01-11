__author__ = 'rdlb'

class Whiskers:
    def __init__(self, leftOne, leftTwo, rightOne, rightTwo):
        self.leftOne = leftOne
        self.leftTwo = leftTwo
        self.rightOne = rightOne
        self.rightTwo = rightTwo

    def read_whiskers(self):
        return WhiskerState(self.leftOne.read() or self.leftTwo.read(), self.rightOne.read() or self.rightTwo.read())


class WhiskerState:
    def __init__(self, left, right):
        self.left = left
        self.right = right
