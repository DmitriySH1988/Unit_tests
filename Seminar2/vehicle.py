class Vehicle:
    def __init__(self, company, model, year_release, num_wheels):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = num_wheels
        self.speed = 0

    def test_drive(self):
        pass

    def park(self):
        self.speed = 0

class Car(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release, num_wheels=4)

    def test_drive(self):
        self.speed = 60

class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release, num_wheels=2)

    def test_drive(self):
        self.speed = 75
