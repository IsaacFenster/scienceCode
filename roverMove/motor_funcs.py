import RPi.GPIO as GPIO          
GPIO.setmode(GPIO.BOARD)

def motor_init (in1, in2, en, freq, dutycycle):
   GPIO.setup(in1,GPIO.OUT)
   GPIO.setup(in2,GPIO.OUT)
   GPIO.setup(en,GPIO.OUT)
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.LOW)
   pwm_pin=GPIO.PWM(en,freq)
   pwm_pin.start(dutycycle)
   return pwm_pin

