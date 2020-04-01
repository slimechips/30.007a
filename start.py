from roboclaw import Roboclaw
from time import sleep
from motorfuncs import MotorFunc

if __name__ == "__main__":
    motorfunc = MotorFunc()        
    motorfunc.moveAll(127)