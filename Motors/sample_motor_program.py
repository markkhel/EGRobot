#Python Script to test motors

import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM) 			#Use Broadcom GPIO numbers instead of using board pi numbers (E.G use GPIO 17 rather then saying use PI pin 0(both correspond to same location on raspberry pi)) 
GPIO.setwarnings(False) 			#Since we can have more than one script/circuit on a single GPIO pin of Raspberry Pi, set False to turn off warnings

in1 = 17				
in2 = 27
ena = 22 				#(motor speed control(PWM=Pulse Width Modulation))
dc = 40.0

#Setup GPIO pins as output to send control signals from the pins to motors 
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

#Set up PWM for controlling motor speed
pwm = GPIO.PWM(ena, 100)
pwm.start(dc)		#start with motor in "off" status

#Initialize motor state and current flow to ensure motors are in stopped state before making them move
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

#read user input, depending on character entered, rotate forward, rotate backward, or end program

#'f' == move forward, 'r' == move reverse, 's' == stop

while(True):
    user_input = input()
    
    if user_input == 'f':
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        
    elif user_input == 'r':
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        
    elif user_input == 's':
        GPIO.cleanup()
        print("clear states of GPIO pins")
        break
    
    else:
        print("Only valid characters to enter are 'f', 'r', and 's'. If you wish to stop the program please enter 's'. ")




