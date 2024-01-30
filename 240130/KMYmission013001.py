import RPi.GPIO as GPIO
import time

LED_RED = 6
LED_GREEN = 5
LED_BLUE = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

GPIO.output(LED_RED, GPIO.LOW)
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_BLUE, GPIO.LOW)

print("3 Color LED Control Start !!")
for i in range(20):
    print("Red LED On !!")
    GPIO.output(LED_RED, GPIO.HIGH)
    time.sleep(0.5)
    
    print("Red LED Off !!\nGreen LED On !!")
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.HIGH)
    time.sleep(0.5)
    
    print("Green LED Off !!\nBlue LED On !!")
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.HIGH)
    time.sleep(0.5)
    
    print("Blue LED Off !!")
    GPIO.output(LED_BLUE, GPIO.LOW)

GPIO.cleanup()
