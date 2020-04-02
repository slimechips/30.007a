from roboclaw import Roboclaw
from time import sleep
from motorfuncs import MotorFunc

if __name__ == "__main__":
  stop = False
  motorfunc = MotorFunc()        
  while not stop:
    key = _GetchUnix()
    if key == 'W':
      motorfunc.moveAll(63)
    elif key == 'A':
      motorfunc.moveAll(31)
    else:
      motorfunc.stopAll()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch