import RPi.GPIO as GPIO          
GPIO.setmode(GPIO.BOARD)


def map(input, og_min, og_max, min, max):
    "Input is value you want converted, ogs are range of that, min/max is range of final value"
    return ((input-og_min)*(max-min))/(og_max-og_min)+min


class RoverMotor:

    def __init__(self, in1, in2, ppin, freq, dc_min, dc_max):
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(ppin,GPIO.OUT)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        self.pwm_pin=GPIO.PWM(ppin,freq)
        self.pwm_pin.start(0)
        self.dc_min = dc_min
        self.dc_max = dc_max

    # vel should be input -100 to 100 
    def change_velocity(self, vel):
        duty_cycle = map(vel, -100, 100, self.dc_min, self.dc_min)
        
        if vel > 0:
            # Make motor go forward
            
