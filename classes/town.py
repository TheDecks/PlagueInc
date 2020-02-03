import random
from typing import List

from classes.agent import Agent
from classes.place import Place


class Town:
    homes: List[Place]
    work_places: List[Place]
    schools: List[Place]
    shopping_centres: List[Place]
    meeting_places: List[Place]
    gyms: List[Place]
    agents: List[Agent]

    def __init__(self, no_homes: int, contamination_length: int):
        self.no_homes = no_homes
        self.homes = []
        self.work_places = []
        self.schools = []
        self.agents = []
        self.shopping_centres = []
        self.meeting_places = []
        self.gyms = []
        self.contamination_length = contamination_length
        self.sick_reports = []
        self.recovered_reports = []
        self.susceptible_reports = []

    def create_homes(self):
        for _ in range(self.no_homes):
            self.homes.append(Place('home', 4, 0, 0, self.contamination_length))

    def create_work_places(self):
        no_agents = 2 * self.no_homes
        currently_created = 0
        while currently_created < no_agents:
            capacity = random.randint(60, 100)
            open_from = random.randint(6, 10)
            self.work_places.append(Place('work place', capacity, open_from, open_from + 12, self.contamination_length))
            currently_created += capacity

    def create_schools(self):
        no_agents = 2 * self.no_homes
        currently_created = 0
        while currently_created < no_agents:
            capacity = random.randint(200, 400)
            self.schools.append(Place('school', capacity, 7, 16, self.contamination_length))
            currently_created += capacity

    def create_shopping_centres(self):
        no_agents = 4 * self.no_homes
        currently_created = 0
        while currently_created < no_agents:
            capacity = random.randint(100, 400)
            self.shopping_centres.append(Place('shopping centre', capacity, 10, 22, self.contamination_length))
            currently_created += capacity

    def create_meeting_places(self):
        no_agents = 4 * self.no_homes
        currently_created = 0
        while currently_created < no_agents:
            capacity = random.randint(20, 70)
            self.meeting_places.append(Place('meeting places', capacity, 11, 19, self.contamination_length))
            currently_created += capacity

    def create_gyms(self):
        no_agents = 4 * self.no_homes
        currently_created = 0
        while currently_created < no_agents:
            capacity = random.randint(20, 70)
            self.gyms.append(Place('gym', capacity, 6, 23, self.contamination_length))
            currently_created += capacity

    def create_agents(self, adult_ill_transfer_probability: float, child_ill_transfer_probability: float,
                      adult_recover_probability: float, child_recover_probability: float):
        # not yet to be done
        for home in self.homes:
            parent_1 = Agent('adult', adult_ill_transfer_probability, adult_recover_probability)
            parent_2 = Agent('adult', adult_ill_transfer_probability, adult_recover_probability)
            child_1 = Agent('child', child_ill_transfer_probability, child_recover_probability)
            child_2 = Agent('child', child_ill_transfer_probability, child_recover_probability)
            parent_1.add_place(home, 0)
            parent_2.add_place(home, 0)
            child_1.add_place(home, 0)
            child_2.add_place(home, 0)
            self.agents.extend([parent_1, parent_2, child_1, child_2])
            home.currently_occupying += 4

    def assign_work_places_and_schools(self):
        facilities_people = {}
        for agent in self.agents:
            if agent.type == 'adult':
                facility_pool = self.work_places
            else:
                facility_pool = self.schools
            facility = random.choice(facility_pool)
            if facility not in facilities_people:
                facilities_people[facility] = 0
            else:
                while facilities_people[facility] >= facility.max_capacity:
                    facility = random.choice(facility_pool)
                    if facility not in facilities_people:
                        facilities_people[facility] = 0
            facilities_people[facility] += 1
            n_route_time = random.randint(facility.open_from, facility.open_from + int(1 / 3 * facility.open_for))
            agent.add_place(facility, n_route_time)
            agent.next_routine_time = n_route_time

    def assign_extracurricular_activities(self):
        for agent in self.agents:
            activity_pool = random.choice([self.shopping_centres, self.meeting_places, self.gyms])
            place = random.choice(activity_pool)
            agent.add_place(place, agent.routine_times[-1] + (8 if agent.type == 'adult' else 6))
            agent.add_place(agent.routine_places[0], agent.routine_times[-1] + random.randint(1, 3))

    def spread_virus(self, initial_probability: float):
        for agent in self.agents:
            if random.random() < initial_probability:
                agent.is_sick = True

    def update_timers(self):
        self.report_values()
        for agent in self.agents:
            agent.proceed()
        for place in (
                self.homes + self.work_places + self.schools + self.gyms + self.meeting_places + self.shopping_centres):
            place.proceed()

    def report_values(self):
        self.sick_reports.append(sum([1 for agent in self.agents if agent.is_sick]))
        self.recovered_reports.append(sum([1 for agent in self.agents if agent.is_recovered]))
        self.susceptible_reports.append(sum(
            [1 for agent in self.agents if not agent.is_sick and not agent.is_recovered]
        ))
