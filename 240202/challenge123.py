import RPi.GPIO as GPIO
import time

SW4 = 25
buzzer_pin = 14

feq = [261, 294, 329, 349, 392, 440, 493, 523]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)
GPIO.setup(SW4, GPIO.IN)

pwm = GPIO.PWM(buzzer_pin,100)

sound = 0
while(1):
    ret = GPIO.input(SW4)
    if ret == 0:
        pwm.start(100)
        pwm.ChangeDutyCycle(20)

        if sound == 0:
            pwm.ChangeFrequency(feq[0])
        elif sound == 1:
            pwm.ChangeFrequency(feq[1])
        elif sound == 2:
            pwm.ChangeFrequency(feq[2])
        elif sound == 3:
            pwm.ChangeFrequency(feq[3])
        elif sound == 4:
            pwm.ChangeFrequency(feq[4])
        elif sound == 5:
            pwm.ChangeFrequency(feq[5])
        elif sound == 6:
            pwm.ChangeFrequency(feq[6])
        elif sound == 7:
            pwm.ChangeFrequency(feq[7])
        elif sound == 8:
            pwm.ChangeFrequency(feq[8])
        elif sound == 9:
            pwm.ChangeFrequency(feq[9])
        elif sound == 10:
            break

        time.sleep(0.5)
        pwm.stop()
        sound += 1

    time.sleep(0.2)
        
pwm.ChangeDutyCycle(0)
pwm.stop()
GPIO.cleanup()