import random
from typing import List

from classes.agent import Agent
from classes.place import Place


class Town:

    homes: List[Place]
    work_places: List[Place]
    schools: List[Place]

    def __init__(self, no_homes: int, contamination_length: int):
        self.no_homes = no_homes
        self.homes = []
        self.work_places = []
        self.schools = []
        self.contamination_length = contamination_length

    def create_homes(self):
        for _ in range(self.no_homes):
            self.homes.append(Place('home', 4, 0, 0, self.contamination_length))

    def create_work_places(self):
        no_agents = 2 * self.no_homes
        currently_created = 0
        while currently_created < no_agents:
            capacity = random.randint(60, 100)
            open_from = random.randint(6, 10)
            self.work_places.append(Place('work place', capacity, open_from, open_from + 10, self.contamination_length))
            currently_created += capacity

    def create_schools(self):
        no_agents = 2 * self.no_homes
        currently_created = 0
        while currently_created < no_agents:
            capacity = random.randint(200, 400)
            self.schools.append(Place('school', capacity, 7, 16, self.contamination_length))
            currently_created += capacity

    def create_agents(self):
        # not yet to be done
        for home in self.homes:
            parent_1 = Agent('parent')
            parent_2 = Agent('parent')
            child_1 = Agent('child')
            child_2 = Agent('child')
            parent_1.add_place()
