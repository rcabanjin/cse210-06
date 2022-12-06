from constants import *
from game.scripting.action import Action


class ControlRacketAction2(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket2 = cast.get_first_actor(RACKET_GROUP_2)
        if self._keyboard_service.is_key_down(LEFT_2): 
            racket2.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT_2): 
            racket2.swing_right()  
        else: 
            racket2.stop_moving()        


            