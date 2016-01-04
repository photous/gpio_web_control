# This app basicly just calls 2 functions (on and off) 
# using 2 Buttons
# This is Awesome
# You can Click On and it will print "IT'S ON!" and switches the GPIO pin On
# You can Click Off and it will print "IT'S OFF!" and switches the GPIO pin On
import RPi.GPIO as GPIO  
import time
from flask import Flask, render_template, request
app = Flask(__name__)

def gpio_on(pin):  
# to use Raspberry Pi board pin numbers
	    GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
	    GPIO.setup(pin, GPIO.OUT)  
##############
            GPIO.output(pin,GPIO.HIGH)
	    return
def gpio_off(pin):
# to use Raspberry Pi board pin numbers
	    GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
	    GPIO.setup(pin, GPIO.OUT)  
##############
	    GPIO.output(pin,GPIO.LOW)
	    return
@app.route('/', methods=['GET', 'POST'])

def root(x=None, y=None):
    # do something to send email
    print "IT'S Root!"
    return render_template('click.html', x=x)


@app.route('/on', methods=['GET', 'POST'])

def on(x=None, y=None):
    # do some other thing 
    print "IT'S ON!"
    # You can change 11 to use a different GPIO pin
    gpio_on(11)
    return render_template('click.html', x=x)

@app.route('/off', methods=['GET', 'POST'])

def off(x=None, y=None):
    # do something to send email
    print "IT'S OFF!"
    # You can change 11 to use a different GPIO pin
    gpio_off(11)
    return render_template('click.html', x=x)

GPIO.cleanup()   
if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
