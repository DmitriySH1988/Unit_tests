# Задание 1. Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли
# переданное число четным или нечетным:


import unittest

class NumberChecker:
    def even_odd_number(self, n):
        return n % 2 == 0

class TestNumberChecker(unittest.TestCase):

    def test_even_odd_number_with_even(self):
        checker = NumberChecker()
        result = checker.even_odd_number(4)
        self.assertTrue(result)

    def test_even_odd_number_with_odd(self):
        checker = NumberChecker()
        result = checker.even_odd_number(3)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
