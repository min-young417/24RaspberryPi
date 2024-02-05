import RPi.GPIO as GPIO
import time
import threading

def fading_green():
    LED_GREEN = 5

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    pwm_green = GPIO.PWM(LED_GREEN, 100) 

    pwm_green.start(0) 

    while True:
        for duty_cycle in range(0, 66):
            pwm_green.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)  
        for duty_cycle in range(65, -1, -1):
            pwm_green.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)

GPIO.setwarnings(False)
GPIO.cleanup()

try:
    thread = threading.Thread(target=fading_green)
    thread.start()

    LED_RED = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_RED, GPIO.OUT)
    pwm_red = GPIO.PWM(LED_RED, 100) 

    pwm_red.start(0) 

    while True:
        for duty_cycle in range(0, 36):
            pwm_red.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)  
        for duty_cycle in range(35, -1, -1):
            pwm_red.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)
            
except KeyboardInterrupt:
    GPIO.cleanup()