import RPi.GPIO as GPIO
GPIO.cleanup()
import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def map(input, og_min, og_max, min, max):
    "Input is value you want converted, ogs are range of that, min/max is range of final value"
    return ((input-og_min)*(max-min))/(og_max-og_min)+min

class Pump():
    """ 
    Pump should be connected to Adafruit PCA9685 16-Channel Servo Driver
    """
    def __init__(self, servo_channel):
        self.servo_channel = servo_channel
    
    def pump_for_time(self, speed, seconds):
        """
        speed: -90 to 90, <0 is CW, >0 is CCW
        seconds: time to run
        """
        speed += 90
        duration = time.time()+seconds
        kit.servo[self.servo_channel].angle = speed
        while time.time()<duration:
            kit.servo[self.servo_channel].angle = 0
            
class Servo():
    """ 
    Servo should be connected to PCA9685 16-Channel Servo Driver
    """
    def __init__(self, servo_channel):
        self.servo_channel = servo_channel

    def rotate_servo(self, degree):
        """
        
        """
        kit.servo[self.servo_channel].angle = degree
        
class DCMotor():
    def __init__(self, in1, in2, enA):
        self.in1 = in1
        GPIO.setup(in1, GPIO.OUT)
        self.in2 = in2
        GPIO.setup(in2, GPIO.OUT)
        self.enA = enA
        GPIO.setup(enA, GPIO.OUT)
        self.pwm = GPIO.PWM(enA, 100)
        self.pwm.start(0)
        # ^ MAY NEED TO BE EDITED FOR FREQUENCY
    
    def dc_for_time(self, direction, speed, seconds):
        """
        direction: "f" or "b"
        speed: 0-100
        seconds: time to run
        """
        if direction == "f":
            print("forward")
            GPIO.output(self.in1, 1)
            GPIO.output(self.in2, 0)
        
        if direction == "b":
            print("backward")
            GPIO.output(self.in1, 0)
            GPIO.output(self.in2, 1)
        
        duration = time.time() + seconds
        self.pwm.ChangeDutyCycle(speed)
        while time.time() < duration:
            continue
        self.pwm.ChangeDutyCycle(0)
    
    def __del__(self):
        self.pwm.stop()
        GPIO.cleanup()
        
