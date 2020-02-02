from typing import List, Union

from classes.place import Place


class Agent:

    routine_places: List[Union[Place, List[Place]]]

    def __init__(self, _type: str):
        self.type = _type
        self.is_using_public_transport = False
        self.routine_places = []
        self.routine_times = []
        self.timer = 0
        self.is_sick = False
        self.is_recovered = False
        self.current_place = None
        self.next_routine_time = None

    def add_place(self, places: Union[Place, List[Place]], time: int):
        self.routine_places.append(places)
        self.routine_times.append(time)

    def proceed(self):
        self.timer += 1
        self.timer = self.timer % 24
