class Place:

    def __init__(self, capacity: int, open_from: int, open_to: int, contamination_length: int):
        self.max_capacity = capacity
        self.currently_occupying = 0
        self.is_contaminated = False
        self.last_contamination_time = None
        self.open_from = open_from
        self.open_to = open_to
        self.open_for = (open_to - open_from) % 24
        self.timer = 0
        self.contamination_length = contamination_length

    def contaminate(self):
        self.is_contaminated = True
        self.last_contamination_time = self.timer

    def decontaminate(self):
        self.is_contaminated = False
        self.last_contamination_time = None

    def is_open(self):
        if self.open_to == self.open_from:
            return True
        return (self.open_from - self.timer) % 24 < self.open_for

    def proceed(self):
        if self.last_contamination_time is not None and (self.timer - self.last_contamination_time) % 24 < self.timer:
            self.decontaminate()
        self.timer += 1
