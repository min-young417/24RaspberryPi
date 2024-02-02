import RPi.GPIO as GPIO

LED_RED = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
pwm = GPIO.PWM(LED_RED, 100)
pwm.start(0)

for i in range(20):
    a = input()

    if a == 't':
        pwm.ChangeDutyCycle(100)

    if a == '0':
        pwm.ChangeDutyCycle(0)

    if a == '5':
        pwm.ChangeDutyCycle(50)

GPIO.cleanup()