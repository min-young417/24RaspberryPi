import RPi.GPIO as GPIO
import time
import threading

def blink_led():
    led_pin = 4  # GPIO 핀 번호

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)

    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)

GPIO.setwarnings(False)
GPIO.cleanup()

# 쓰레딩으로 LED 깜빡임 함수 실행
thread = threading.Thread(target=blink_led)
thread.start()

while True:
    print("main")
    time.sleep(1)