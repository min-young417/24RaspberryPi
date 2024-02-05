import RPi.GPIO as GPIO
import time
import threading

def blink_green():
    LED_GREEN = 5  # LED_GREEN - GPIO_05

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_GREEN, GPIO.OUT)

    while True:
        GPIO.output(LED_GREEN, GPIO.HIGH)
        time.sleep(0.65)
        GPIO.output(LED_GREEN, GPIO.LOW)
        time.sleep(0.65)

def blink_blue():
    LED_BLUE = 6   # LED_BLUE - GPIO_06

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_BLUE, GPIO.OUT)

    while True:
        GPIO.output(LED_BLUE, GPIO.HIGH)
        time.sleep(0.85)
        GPIO.output(LED_BLUE, GPIO.LOW)
        time.sleep(0.85)

GPIO.setwarnings(False)
GPIO.cleanup()

try:
    thread1 = threading.Thread(target=blink_green)
    thread1.start()

    thread2 = threading.Thread(target=blink_blue)
    thread2.start()

    LED_RED = 4    # LED_RED - GPIO_04

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_RED, GPIO.OUT)

    while True:
        GPIO.output(LED_RED, GPIO.HIGH)
        time.sleep(0.35)
        GPIO.output(LED_RED, GPIO.LOW)
        time.sleep(0.35)

except KeyboardInterrupt:
    GPIO.cleanup()
