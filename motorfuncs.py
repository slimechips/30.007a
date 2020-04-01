from roboclaw import Roboclaw
from time import sleep

address = 0x80
m1Dir = 1
m2Dir = 1

class MotorFunc:
  def __init__(self):
    self.roboclaw = Roboclaw("/dev/ttyS0", 38400)
    self.roboclaw.Open()
    self.addr = address
    self.m1Dir = m1Dir
    self.m2Dir = m2Dir

  def _forwardM1(self, val=127):
    evalVal = val * self.m1Dir
    if evalVal < 0:
      self.roboclaw.BackwardM1(self.addr, evalVal)
    else:
      self.roboclaw.ForwardM1(self.addr, evalVal)

  def _forwardM2(self, val=127):
    evalVal = val * self.m2Dir
    if val < 0:
      self.roboclaw.BackwardM2(self.addr, evalVal)
    else:
      self.roboclaw.ForwardM2(self.addr, evalVal)

  def moveAll(self, val=127):
    self._forwardM1(val)
    self._forwardM2(val)

  def moveM1Only(self, val=127):
    self._forwardM1(val)
    self._forwardM2(0)

  def moveM2Only(self, val=127):
    self._forwardM1(0)
    self._forwardM2(val)

  def stopAll(self):
    self._forwardM1(0)
    self._forwardM2(0)

  def brakeAll(self):
    self._forwardM1(1)
    self._forwardM2(1)