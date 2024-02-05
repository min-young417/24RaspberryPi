from flask import Flask, render_template, url_for, redirect   # url_for 함수, redirect 함수 추가
import RPi.GPIO as GPIO

app = Flask(__name__)

red = 4
green = 5
blue = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)
GPIO.output(blue, GPIO.LOW)

led_states = {                           # 전체 led의 현황 표시용
    'red':0,
    'green':0,
    'blue':0
}

@app.route('/')                       # 기본주소('/')로 들어오면
def home():
    return render_template('index.html', led_states=led_states)   # index.html에 전체 led현황을 함께 전달 

@app.route('/<color>/<int:state>')                                # 개별 led를 켜고 끄는 주소
def led_switch(color, state):                                    # 개별 led ON, OFF 함수
    led_states[color] = state 
    if color == 'red':
        GPIO.output(red, state) 
    elif color == 'green':
        GPIO.output(green, state) 
    elif color == 'blue':
        GPIO.output(blue, state) 
    return redirect(url_for('home'))                           # leds의 색상변경이 완료되면 redirect함수를 통해 기본주소('/')으로 이동

@app.route('/all/<int:state>')                                 # 모든 led를 한꺼번에 켜거나 끄는 주소
def all_on_off(state):                                         # 모든 led를 한꺼번에 켜거나 끄는 함수
    led_states['red'] = state
    led_states['green'] = state
    led_states['blue'] = state 
    GPIO.output(red, state)
    GPIO.output(green, state)
    GPIO.output(blue, state)
    return redirect(url_for('home'))                     # 모든 led를 켜거나 껐으면 기본주소('/')로 이동

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
