import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)

try:
    while True:
        a = input()

        pwm.start(100)
        pwm.ChangeDutyCycle(20)

        if a == 'q':
            pwm.ChangeDutyCycle(3.0)
        elif a == 'w':
            pwm.ChangeDutyCycle(7.5)
        elif a == 'e':
            pwm.ChangeDutyCycle(12.5)
            
        time.sleep(1.0)
        pwm.ChangeDutyCycle(0.0)    
        pwm.stop()

except KeyboardInterrupt:
    GPIO.cleanup()