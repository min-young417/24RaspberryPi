import RPi.GPIO as GPIO
import time

LED_RED = 4
SW4 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(SW4, GPIO.IN)
GPIO.output(LED_RED, GPIO.LOW)

light = 0
try:
    while True:
        ret = GPIO.input(SW4)
        if ret == 0:
            if light == 0:
                GPIO.output(LED_RED, GPIO.HIGH)
                light = 1
            elif light == 1:
                GPIO.output(LED_RED, GPIO.LOW)
                light = 0

        time.sleep(0.2)

except KeyboardInterrupt:        
    GPIO.cleanup()