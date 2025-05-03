from browser_use.controller.service import Controller

from utils.Posts import Posts

class ControllerInstance:

    def controller(self):
        control = Controller(output_model=Posts)
        return control
