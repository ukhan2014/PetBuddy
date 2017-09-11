import RPi.GPIO as GPIO
import time

def update(angle):
  duty = float(angle) / 10.0 + 2.5
  pwm.ChangeDutyCycle(duty)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

open = 0

while(1):
  if(open == 0):
    angle = 93
    update(angle)
    open = 1
  else:
    angle = 0
    update(angle)
    open = 0

  time.sleep(5)
