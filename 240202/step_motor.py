import RPi.GPIO as GPIO
import time

STEP_OUTA = 16
STEP_OUTB = 17
STEP_OUT2A = 18
STEP_OUT2B = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_OUTA, GPIO.OUT)
GPIO.setup(STEP_OUTB, GPIO.OUT)
GPIO.setup(STEP_OUT2A, GPIO.OUT)
GPIO.setup(STEP_OUT2B, GPIO.OUT)

try:
    for i in range(2000):
        GPIO.output(STEP_OUTA, GPIO.HIGH)
        time.sleep(0.002)
        GPIO.output(STEP_OUTA, GPIO.LOW)
        GPIO.output(STEP_OUTB, GPIO.HIGH)
        time.sleep(0.002)
        GPIO.output(STEP_OUTB, GPIO.LOW)
        GPIO.output(STEP_OUT2A, GPIO.HIGH)
        time.sleep(0.002)
        GPIO.output(STEP_OUT2A, GPIO.LOW)
        GPIO.output(STEP_OUT2B, GPIO.HIGH)
        time.sleep(0.002)
        GPIO.output(STEP_OUT2B, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
