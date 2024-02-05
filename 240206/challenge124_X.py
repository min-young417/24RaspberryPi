import RPi.GPIO as GPIO
import time

SW4 = 25
servo_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(SW4, GPIO.IN)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)

servo = 0
try:
    while True:
        ret = GPIO.input(SW4)
        if ret == 0:
            if servo == 0:
                pwm.ChangeDutyCycle(0)
            elif servo == 1:
                pwm.ChangeDutyCycle(50)
            elif servo == 2:
                pwm.ChangeDutyCycle(100)
            elif servo == 3:
                break
            
            servo += 1
        
        time.sleep(0.2)
        
except KeyboardInterrupt:
    GPIO.cleanup()