import random
from typing import List

from classes.place import Place


class Agent:

    routine_places: List[Place]
    id: int = 0

    def __init__(self, _type: str, ill_transfer_probability: float, recover_probability: float):
        self.type = _type
        self.is_using_public_transport = False
        self.routine_places = []
        self.routine_times = []
        self.timer = 0
        self.is_sick = False
        self.is_recovered = False
        self.current_place = 0
        self.next_routine_time = None
        self.ill_transfer_probability = ill_transfer_probability
        self.recover_probability = recover_probability
        self.id = Agent.id
        Agent.id += 1

    def add_place(self, places: Place, time: int):
        self.routine_places.append(places)
        self.routine_times.append(time)

    def proceed(self):
        self.timer += 1
        self.timer = self.timer % 24
        if self.timer == 0 and self.is_sick and random.random() < self.recover_probability:
            self.is_sick = False
            self.is_recovered = True
            self.ill_transfer_probability = 0
        if self.routine_places[self.current_place].is_contaminated and random.random() < self.ill_transfer_probability:
            self.is_sick = True
        if self.is_sick:
            current_place = self.routine_places[self.current_place]
            current_place.contaminate()
        if self.timer >= self.next_routine_time:
            self.routine_places[self.current_place].currently_occupying -= 1
            self.current_place += 1
            self.current_place %= len(self.routine_times)
            self.next_routine_time = self.routine_times[(self.current_place + 1) % len(self.routine_times)]
            while (self.routine_places[self.current_place].is_full() or
                   not self.routine_places[self.current_place].is_open()):
                self.current_place += 1
                self.current_place %= len(self.routine_times)
                self.next_routine_time = self.routine_times[(self.current_place + 1) % len(self.routine_times)]
            self.routine_places[self.current_place].currently_occupying += 1
