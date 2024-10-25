import pygame
import RPi.GPIO as GPIO
import time

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

GPIO.setmode(GPIO.BCM)
leftMotorForward = 17
leftMotorBackward = 18
rightMotorForward = 19
rightMotorBackward = 20
GPIO.setup([leftMotorForward, leftMotorBackward, rightMotorForward, rightMotorBackward], GPIO.OUT)

def controlMotors(left_speed, right_speed):
    
    if left_speed > 0:
        GPIO.output(leftMotorForward, GPIO.HIGH)
        GPIO.output(leftMotorBackward, GPIO.LOW)
    
    elif left_speed < 0:
        GPIO.output(leftMotorForward, GPIO.LOW)
        GPIO.output(leftMotorBackward, GPIO.HIGH)
    
    else:
        GPIO.output(leftMotorForward, GPIO.LOW)
        GPIO.output(leftMotorBackward, GPIO.LOW)
        
    if right_speed > 0:
        GPIO.output(rightMotorForward, GPIO.HIGH)
        GPIO.output(rightMotorBackward, GPIO.LOW)
    
    elif right_speed < 0:
        GPIO.output(rightMotorForward, GPIO.LOW)
        GPIO.output(rightMotorBackward, GPIO.HIGH)
    
    else:
        GPIO.output(rightMotorForward, GPIO.LOW)
        GPIO.output(rightMotorBackward, GPIO.LOW)

def stopMotors():
    controlMotors(0, 0)

try:
    while True:
        pygame.event.pump()
                
        triangle = joystick.get_button(3)  # Triangle
        square = joystick.get_button(0)     # Square
        circle = joystick.get_button(1)     # Circle
        cross = joystick.get_button(2)      # Cross

        if triangle:  # Forward
            controlMotors(25, 25)
        
        if square:  # Left
            controlMotors(-25, 25)
        
        if circle:  # Right
            controlMotors(25, -25)
        
        if cross:   # Backward
            controlMotors(-25, -25)
        
        else:  # Stop
            stopMotors()

        time.sleep(0.1)

except KeyboardInterrupt:
    stopMotors()
    GPIO.cleanup()
    pygame.quit()
