from pyPS4Controller.controller import Controller
    
    
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


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
