import unittest
from vehicle import Vehicle, Car, Motorcycle

class TestVehicle(unittest.TestCase):

    def test_car_is_instance_of_vehicle(self):
        car = Car("Company", "Model", 2023)
        self.assertIsInstance(car, Vehicle)

    def test_car_has_four_wheels(self):
        car = Car("Company", "Model", 2023)
        self.assertEqual(car.num_wheels, 4)

    def test_motorcycle_has_two_wheels(self):
        motorcycle = Motorcycle("Company", "Model", 2023)
        self.assertEqual(motorcycle.num_wheels, 2)

    def test_car_can_drive(self):
        car = Car("Company", "Model", 2023)
        car.test_drive()
        self.assertEqual(car.speed, 60)

    def test_motorcycle_can_drive(self):
        motorcycle = Motorcycle("Company", "Model", 2023)
        motorcycle.test_drive()
        self.assertEqual(motorcycle.speed, 75)

    def test_car_can_park(self):
        car = Car("Company", "Model", 2023)
        car.test_drive()
        car.park()
        self.assertEqual(car.speed, 0)

    def test_motorcycle_can_park(self):
        motorcycle = Motorcycle("Company", "Model", 2023)
        motorcycle.test_drive()
        motorcycle.park()
        self.assertEqual(motorcycle.speed, 0)

if __name__ == '__main__':
    unittest.main()
