import RPi.GPIO as GPIO
import time

SW1 = 22
SW2 = 23
SW3 = 24
SW4 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)

while(1):
    ret = GPIO.input(SW1)
    if ret == 0:
        print("SW1 Button push !!")
    
    ret = GPIO.input(SW2)
    if ret == 0:
        print("SW2 Button push !!")
    
    ret = GPIO.input(SW3)
    if ret == 0:
        print("SW3 Button push !!")
    
    ret = GPIO.input(SW4)
    if ret == 0:
        print("SW4 Button push !!")
    
    time.sleep(1)

GPIO.cleanup()