import RPi.GPIO as GPIO
import time

SW4 = 25
STEP_OUTA = 16
STEP_OUTB = 17
STEP_OUT2A = 18
STEP_OUT2B = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW4, GPIO.IN)
GPIO.setup(STEP_OUTA, GPIO.OUT)
GPIO.setup(STEP_OUTB, GPIO.OUT)
GPIO.setup(STEP_OUT2A, GPIO.OUT)
GPIO.setup(STEP_OUT2B, GPIO.OUT)

def rotate_motor(step):
    for i in range(step): # 130 - 90도, 260 - 180도 
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

degree = 0
try:
    while True:
        ret = GPIO.input(SW4)
        if ret == 0:
            if degree == 0:
                rotate_motor(0)
                degree = 1
            elif degree == 1:
                rotate_motor(130)
                degree = 2
            elif degree == 2:
                rotate_motor(260)
                degree = 0

        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
