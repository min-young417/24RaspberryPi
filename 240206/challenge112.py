import RPi.GPIO as GPIO

LED_RED = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
pwm = GPIO.PWM(LED_RED, 100)
pwm.start(0)

try:
    while True:
        a = input()

        if a == 't':
            pwm.ChangeDutyCycle(100)
        elif a == '0':
            pwm.ChangeDutyCycle(0)
        elif a == '5':
            pwm.ChangeDutyCycle(50)
            
except KeyboardInterrupt:
    GPIO.cleanup()