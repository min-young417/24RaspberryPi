import RPi.GPIO as GPIO

LED_RED = 4 #LED_RED - GPIO_4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

try:
    while True:
        a = input()

        if a == 'n' or a == 'N':   # 입력받은 a가 N이면 LED 켜짐
            GPIO.output(LED_RED, GPIO.HIGH)
        elif a == 'f' or a == 'F': # 입력받은 a가 F면 LED 꺼짐 
            GPIO.output(LED_RED, GPIO.LOW)
             
except KeyboardInterrupt:
    GPIO.cleanup()