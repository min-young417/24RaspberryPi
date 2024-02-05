import RPi.GPIO as GPIO
import time
import threading

def fading_led():
    led_pin = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    pwm_led = GPIO.PWM(led_pin, 100)  # PWM 객체 생성, 주파수는 100Hz로 설정

    pwm_led.start(0)  # PWM 시작, 초기 듀티 사이클 0

    while True:
        for duty_cycle in range(0, 101):
            pwm_led.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)  # 0.01초마다 변화
        for duty_cycle in range(100, -1, -1):
            pwm_led.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)

GPIO.setwarnings(False)
GPIO.cleanup()

# 쓰레딩으로 LED 서서히 켜고 끄는 함수 실행
thread = threading.Thread(target=fading_led)
thread.start()

while True:
    print("main")
    time.sleep(1)