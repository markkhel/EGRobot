import RPi.GPIO as GPIO          
from time import sleep
from pyPS4Controller.controller import Controller
import os  # To open and close files

GPIO.setmode(GPIO.BOARD)

in1 = 18
in2 = 16
en = 22
in3 = 15
in4 = 7
enb = 11
temp1=1

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

p = GPIO.PWM(en, 4)
p2 = GPIO.PWM(enb, 4)
p.start(30)
p2.start(30)

print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.new_file = "SpeechV2.py"  # This is the file you want to open
        self.file_open = False

    # Add the share button functionality
    def open_file(self, file_path):
        """Open the file using Python 3 on Raspberry Pi OS."""
        os.system(f"python3 {file_path} &")  # Run the script in the background

    def close_file(self):
        """Close the Python process running SpeechV2.py."""
        os.system("pkill -f SpeechV2.py")  # Kills the Python process by filename

    def on_share_press(self):
        """When Share button is pressed, open the new file."""
        print("Opening SpeechV2.py...")
        self.open_file(self.new_file)
        self.file_open = True

    def on_share_release(self):
        """When Share button is released, close the new file."""
        if self.file_open:
            print("Closing SpeechV2.py...")
            self.close_file()
            self.file_open = False

    # Driving forwards
    def on_triangle_press(self):
       p.ChangeDutyCycle(40)
       p2.ChangeDutyCycle(40)
       GPIO.output(in1, GPIO.HIGH)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.HIGH)
       GPIO.output(in4, GPIO.LOW)

    def on_triangle_release(self):
       GPIO.output(in1, GPIO.LOW)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.LOW)
       GPIO.output(in4, GPIO.LOW)

    # Driving backwards
    def on_x_press(self):
       p.ChangeDutyCycle(40)
       p2.ChangeDutyCycle(40)
       GPIO.output(in1, GPIO.LOW)
       GPIO.output(in2, GPIO.HIGH)
       GPIO.output(in3, GPIO.LOW)
       GPIO.output(in4, GPIO.HIGH)

    def on_x_release(self):
       GPIO.output(in1, GPIO.LOW)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.LOW)
       GPIO.output(in4, GPIO.LOW)

    # Turning left
    def on_square_press(self):
       p.ChangeDutyCycle(40)
       p2.ChangeDutyCycle(40)
       GPIO.output(in1, GPIO.LOW)
       GPIO.output(in2, GPIO.HIGH)
       GPIO.output(in3, GPIO.HIGH)
       GPIO.output(in4, GPIO.LOW)

    def on_square_release(self):
       GPIO.output(in1, GPIO.LOW)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.LOW)
       GPIO.output(in4, GPIO.LOW)

    # Turning right
    def on_circle_press(self):
       p.ChangeDutyCycle(40)
       p2.ChangeDutyCycle(40)
       GPIO.output(in1, GPIO.HIGH)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.LOW)
       GPIO.output(in4, GPIO.HIGH)

    def on_circle_release(self):
       GPIO.output(in1, GPIO.LOW)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.LOW)
       GPIO.output(in4, GPIO.LOW)
       
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before the controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
