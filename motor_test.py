import motor_objects as motor
import time

pump_speed = 50 # -90 to 90
motor_speed = 50 # 0 - 100

# # TESTING PUMP 
# pump0 = motor.Pump(0)
# pump0.pump_for_time(pump_speed, 2)

# TESTING DC MOTOR
motor1 = motor.DCMotor(in1 = 29, in2 = 31, enA = 32)

motor2 = motor.DCMotor(in1 = 33, in2 = 37, enA = 35)


def test_servo():
    servo_num = input("Enter servo number, STOP to stop: ")
    while(servo_num != "STOP"):
        angle = input("Enter angle: ")
        servo = motor.Servo(servo_num)
        servo.rotate_servo(angle)
        time.sleep(2)
        servo.rotate_servo(0)
        servo_num = input("Enter servo number, STOP to stop: ")

def test_motor():
    motor_num = input("Enter motor number (1-2), STOP to stop: ")
    while(motor_num != "STOP"):
        direction = input("Enter direction (f, b): ")
        if(motor_num == 1):
            motor1.dc_for_time(direction, motor_speed, 1)
        elif(motor_num == 2):
            motor2.dc_for_time(direction, motor_speed, 1)
        motor_num = input("Enter motor number (1-2), STOP to stop: ")


# motor1.dc_for_time("f", motor_speed, 1)
# motor2.dc_for_time("f", motor_speed, 1)


# test_servo()
# test_motor()