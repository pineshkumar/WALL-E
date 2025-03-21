import RPi.GPIO as GPIO
import time

# Define motor control pins
MOTOR_PIN_1 = 17  # Forward
MOTOR_PIN_2 = 27  # Backward
PWM_PIN = 22  # Speed Control (PWM)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN_1, GPIO.OUT)
GPIO.setup(MOTOR_PIN_2, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

# PWM for speed control
pwm = GPIO.PWM(PWM_PIN, 1000)  # 1KHz frequency
pwm.start(0)  # Initially off

def move_forward(speed=100):
    GPIO.output(MOTOR_PIN_1, GPIO.HIGH)
    GPIO.output(MOTOR_PIN_2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def stop_motor():
    GPIO.output(MOTOR_PIN_1, GPIO.LOW)
    GPIO.output(MOTOR_PIN_2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

def move_slow():
    move_forward(speed=40)  # 40% speed

try:
    print("Motor module ready.")
except KeyboardInterrupt:
    GPIO.cleanup()
