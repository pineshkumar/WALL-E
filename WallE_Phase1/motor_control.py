import RPi.GPIO as GPIO
import time

# GPIO Pin Setup
IN1 = 17
IN2 = 27
ENA = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

pwm = GPIO.PWM(ENA, 1000)  # PWM Frequency 1000Hz
pwm.start(0)

def start_motor(speed=100):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)  # Speed control

def stop_motor():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

def slow_motor():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(50)  # Run at 50% speed

if __name__ == "__main__":
    try:
        start_motor()
        time.sleep(5)
        slow_motor()
        time.sleep(5)
        stop_motor()
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
