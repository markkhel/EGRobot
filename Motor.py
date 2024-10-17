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

def control_motors(left_speed, right_speed):
    
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

try:
    while True:
        pygame.event.pump()
        
        left_speed = joystick.get_axis(1)
        right_speed = joystick.get_axis(4)
        
        control_motors(-left_speed * 100, -right_speed * 100)
        
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    pygame.quit()
