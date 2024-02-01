import RPi.GPIO as GPIO
import time
import threading

def play_melody():
    GPIO.setwarnings(False)
    buzzer_pin = 14

    feq = [131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247,
           261, 277, 294, 311, 329, 349, 369, 392, 415, 440, 466, 493, 
           523, 554, 587, 622, 659, 698, 739, 783, 830, 880, 932, 987, 
           1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976]

    num = [20, 25, 34, 25, 27, 25, 27, 29, 30, 29, 22, 27, 27, 25, 25, 25, 24, 22, 24, 
	    25, 20, 20, 25, 24, 25, 27, 25, 27, 29, 30, 29, 22, 27, 27, 25, 25, 25, 24, 22, 24, 
	    25]
    sle = [0.6, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 
	    1.8, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 
	    1.8]

    def play():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buzzer_pin, GPIO.OUT)
        pwm = GPIO.PWM(buzzer_pin, 100)
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

    melody_thread = threading.Thread(target=play)
    melody_thread.start()