import RPi.GPIO as GPIO
import time

PIR_D = 27
BUZZER = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_D, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

for _ in range(20):
    pir_val = GPIO.input(PIR_D)
    if pir_val == 1:
        print("PIR Detected !!")
        GPIO.output(BUZZER, pir_val)
    else:
        print("PIR Not detected !!")
        GPIO.output(BUZZER, pir_val)
    time.sleep(1)

GPIO.output(BUZZER, 0)
GPIO.cleanup()