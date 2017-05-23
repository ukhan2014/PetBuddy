from flask import Flask, render_template
import RPi.GPIO as gpio
import time

app = Flask(__name__)

@app.route('/feedPet')
def feedPet():
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)
    gpio.output(23, 1)
    print("feeding pet")
    time.sleep(1)
    gpio.output(23, 0)
    print("done feeding pet")
    return render_template('index.html')

@app.route("/")
def main():
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)
    time.sleep(1)
    gpio.output(23,0)
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)   
    # app.run(host= '0.0.0.0', port='6000') 

