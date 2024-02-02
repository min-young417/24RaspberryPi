import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
buzzer_pin = 14

feq = [261, 294, 329, 349, 392, 440, 493, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin,100)
	
for i in range(10):
    a = input()

    pwm.start(100)
    pwm.ChangeDutyCycle(20)

    if a == 'a':
        pwm.ChangeFrequency(feq[0])
        time.sleep(0.5)
    
    if a == 's':
        pwm.ChangeFrequency(feq[1])
        time.sleep(0.5)
    
    if a == 'd':
        pwm.ChangeFrequency(feq[2])
        time.sleep(0.5)

    if a == 'f':
        pwm.ChangeFrequency(feq[3])
        time.sleep(0.5)

    if a == 'g':
        pwm.ChangeFrequency(feq[4])
        time.sleep(0.5)

    if a == 'r':
        pwm.ChangeFrequency(feq[5])
        time.sleep(0.5)


    if a == 'l':
        pwm.ChangeFrequency(feq[6])
        time.sleep(0.5)

    if a == 'k':
        pwm.ChangeFrequency(feq[7])
        time.sleep(0.5)
    
    pwm.stop()

GPIO.cleanup()