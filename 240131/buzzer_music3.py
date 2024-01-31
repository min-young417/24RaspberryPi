import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
buzzer_pin = 14

feq = [131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247,
       261, 277, 294, 311, 329, 349, 369, 392, 415, 440, 466, 493, 
       523, 554, 587, 622, 659, 698, 739, 783, 830, 880, 932, 987, 
       1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976]

# 1  도 3  레 5  미 6  파 8  솔 10 라 12 시 3옥
# 13 도 15 레 17 미 18 파 20 솔 22 라 24 시 4옥
# 25 도 27 레 29 미 30 파 32 솔 34 라 36 시 5옥 

# RE:WIND
num = [13, 25, 25, 24, 20, 17, 17, 20, 18, 20, 27, 25, 27, 29, 48, 27, 25, 48, 
	24, 25, 27, 25, 24, 25, 48, 24, 25, 27, 29, 27, 25, 48, 25, 30, 29, 48, 
	32, 29, 27, 15, 24]
sle = [0.6, 0.6, 0.3, 0.6, 0.6, 0.6, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.9, 0.6, 0.3, 1.5, 0.3,
	0.3, 0.3, 0.6, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 1.5, 1.5, 
       0.6, 0.6, 0.6, 0.6, 0.6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin,100)
pwm.start(100)
pwm.ChangeDutyCycle(20)
	
for i in range(len(num)):
    if num[i] == 48:
       pwm.stop()
       time.sleep(sle[i])
       pwm.start(100)
       pwm.ChangeDutyCycle(20)
    else:
       pwm.ChangeFrequency(feq[num[i]])
       time.sleep(sle[i])
	
pwm.stop()
GPIO.cleanup()