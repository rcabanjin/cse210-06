from constants import *
from game.scripting.action import Action


class ControlRacketAction1(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET_GROUP_1)
        if self._keyboard_service.is_key_down(LEFT): 
            racket1.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            racket1.swing_right()  
        else: 
            racket1.stop_moving()        


            