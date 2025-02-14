import time
from adafruit_servokit import ServoKit

def servo_test():
    # MOVES SERVO AT CHANNEL 0 TO SPECIFIED ANGLE
    kit = ServoKit(channels=16)

    while True:
        a = input("enter angle, STOP to stop: ")
        if a == "STOP":
            quit()
        kit.servo[0].angle =int(a)

# For pump clockwise is <90, counter clockwise is >90


servo_test()


