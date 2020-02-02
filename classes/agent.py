from typing import List, Union

from classes.place import Place


class Agent:

    routine_places: List[Union[Place, List[Place]]]

    def __init__(self):

        self.is_using_public_transport = False
        self.routine_places = []
        self.routine_times = []
        self.timer = 0
        self.is_sick = False
        self.current_place = None
        self.next_routine_time = None

    def proceed(self):
        self.timer += 1
