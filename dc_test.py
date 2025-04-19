import RPi.GPIO as GPIO
import time
in1 = 29
in2 = 31
enA = 32

# in1 = 33
# in2 = 37
# enA = 35

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
pwm = GPIO.PWM(enA, 100)
pwm.start(0)

time.sleep(1)

GPIO.output(in1, 1)
GPIO.output(in2, 0)

pwm.ChangeDutyCycle(50)
time.sleep(1)
pwm.ChangeDutyCycle(0)



