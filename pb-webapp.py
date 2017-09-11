from flask import Flask, render_template
import RPi.GPIO as gpio
import time

app = Flask(__name__)

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
pwm = gpio.PWM(18, 100)

def update(angle):
  duty = float(angle) / 10.0 + 2.5
  pwm.ChangeDutyCycle(duty)

@app.route('/feedPet')
def feedPet():
  update(93)
  time.sleep(0.5)
  update(0)

  #we can set pwm to 0 to stop servo from making noise
  #at the closed position
  #time.sleep(1)
  #pwm.ChangeDutyCycle(0)
  print("done feeding pet")
  return render_template('index.html')


@app.route("/")
def main():
  pwm.start(5)
  time.sleep(1)
  return render_template('index.html')
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(host='0.0.0.0', port=8070, debug=True)
    
