# Задание 2. Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли
# переданное число в интервал (25;100)
# public boolean numberInInterval(int n) { … }


import unittest


class NumberChecker:
    def number_in_interval(self, n):
        return 25 < n < 100


class TestNumberChecker(unittest.TestCase):

    def test_number_in_interval_inside(self):
        checker = NumberChecker()
        result = checker.number_in_interval(50)
        self.assertTrue(result)

    def test_number_in_interval_outside(self):
        checker = NumberChecker()
        result = checker.number_in_interval(10)
        self.assertFalse(result)

    def test_number_in_interval_edge_case_lower_bound(self):
        checker = NumberChecker()
        result = checker.number_in_interval(26)
        self.assertTrue(result)

    def test_number_in_interval_edge_case_upper_bound(self):
        checker = NumberChecker()
        result = checker.number_in_interval(99)
        self.assertTrue(result)

    def test_number_in_interval_edge_case_below_lower_bound(self):
        checker = NumberChecker()
        result = checker.number_in_interval(25)
        self.assertFalse(result)

    def test_number_in_interval_edge_case_above_upper_bound(self):
        checker = NumberChecker()
        result = checker.number_in_interval(100)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
