import RPi.GPIO as gpio
import time
from config import FREQUENCY, DUTY_CYCLE, ENA, ENB, IN1, IN2, IN3, IN4

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(IN1, gpio.OUT)
	gpio.setup(IN2, gpio.OUT)
	gpio.setup(IN3, gpio.OUT)
	gpio.setup(IN4, gpio.OUT)
	gpio.setup(ENB, gpio.OUT)
	gpio.setup(ENA, gpio.OUT)
	

def right(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)
	gpio.output(IN1, True)
	gpio.output(IN2, False)
	gpio.output(IN3, True)
	gpio.output(IN4, False)
	time.sleep(tf)
	gpio.cleanup()

def left(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)
	gpio.output(IN1, False)
	gpio.output(IN2, True)
	gpio.output(IN3, False)
	gpio.output(IN4, True)
	time.sleep(tf)
	gpio.cleanup()

def forward(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)	
	gpio.output(IN1, False)
	gpio.output(IN2, True)
	gpio.output(IN3, True)
	gpio.output(IN4, False)
	time.sleep(tf)
	gpio.cleanup()

def reverse(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)
	gpio.output(IN1, True)
	gpio.output(IN2, False)
	gpio.output(IN3, False)
	gpio.output(IN4, True)
	time.sleep(tf)
	gpio.cleanup()

if __name__ == '__main__':
	forward(1)
	left(1.5)
	forward(1)
	left(1.5)
	forward(1)
	left(1.5)
	forward(1)
