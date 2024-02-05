import RPi.GPIO as GPIO
import time

LED_RED = 4
SW4 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(SW4, GPIO.IN)

pwm = GPIO.PWM(LED_RED, 100)
pwm.start(0)

light = 0
try:
    while True:
        ret = GPIO.input(SW4)
        if ret == 0:
            if light == 0:
                pwm.ChangeDutyCycle(0)
                light = 1
            elif light == 1:
                pwm.ChangeDutyCycle(50)
                light = 2
            elif light == 2:
                pwm.ChangeDutyCycle(100)
                light = 0
        
        time.sleep(0.2)
        
except KeyboardInterrupt:   
    GPIO.cleanup()