import RPi.GPIO as GPIO          
from time import sleep
from pyPS4Controller.controller import Controller
GPIO.setmode(GPIO.BOARD)

in1 = 18
in2 = 16
en = 22
in3 = 15
in4 = 7
enb = 11
temp1=1

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p=GPIO.PWM(en,4)
p2=GPIO.PWM(enb,4)

p.start(30)
p2.start(30)

print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_release(self):
       print("helloooooooooooooooooooooooooooooooooooooooooooo")

    def on_x_release(self):
       pass
       # print("Goodbye worlddddddddddddddddddddddddddddddddddddd")

    def on_R3_up(self):
       pass
       # print("Please")

    def on_R3_down(self,arg):
       pass
       # print("Please")



    def on_L3_up(self,arg):
       pass
       # print("yhjkyujktyghjmthgmtyuhjkmyuj")

    def on_L3_down(self,arg):
       pass

    def on_L3_left(self,arg):
       pass

    def on_L3_right(self,arg):
       pass

    def on_R3_up(self,arg):
       pass

    def on_R3_left(self,arg):
       pass

    def on_R3_right(self,arg):
       pass
    def on_R3_x_at_rest(self):
       pass 
    def on_R3_y_at_rest(self):
       pass
    def on_L3_x_at_rest(self):
       pass 
    def on_L3_y_at_rest(self):
       pass
    def on_triangle_press(self):
       p.ChangeDutyCycle(40)
       p2.ChangeDutyCycle(40)
       GPIO.output(in1,GPIO.HIGH)
       GPIO.output(in2,GPIO.LOW)
       GPIO.output(in3, GPIO.HIGH)
       GPIO.output(in4, GPIO.LOW)

    def on_triangle_release(self):
       GPIO.output(in1,GPIO.LOW)
       GPIO.output(in2,GPIO.LOW)
       GPIO.output(in3, GPIO.LOW)
       GPIO.output(in4, GPIO.LOW)
       
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
