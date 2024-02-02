import RPi.GPIO as GPIO

LED_RED = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

for i in range(20):
    a = input()

    if a == 'n' or a == 'N':
        GPIO.output(LED_RED, GPIO.HIGH)

    if a == 'f' or a == 'F':
        GPIO.output(LED_RED, GPIO.LOW)

GPIO.cleanup()