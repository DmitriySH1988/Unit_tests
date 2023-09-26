class Calculator:
    @staticmethod
    def calculate_discount(purchase_amount, discount_percentage):
        if purchase_amount < 0 or discount_percentage < 0 or discount_percentage > 100:
            raise ArithmeticError("Invalid input")
        return purchase_amount - (purchase_amount * (discount_percentage / 100))


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Shop:
    def __init__(self, products):
        self.products = products

    def sort_products_by_price(self):
        self.products.sort(key=lambda x: x.price)

    def get_most_expensive_product(self):
        if not self.products:
            raise ValueError("No products in the shop")
        return max(self.products, key=lambda x: x.price)


# Тест с использованием библиотеки unittest

import unittest

class TestShop(unittest.TestCase):

    def test_sort_products_by_price(self):
        products = [
            Product("Product A", 50.0),
            Product("Product B", 30.0),
            Product("Product C", 70.0)
        ]
        shop = Shop(products)
        shop.sort_products_by_price()
        self.assertEqual(shop.get_most_expensive_product().name, "Product C")

    def test_get_most_expensive_product(self):
        products = [
            Product("Product A", 50.0),
            Product("Product B", 30.0),
            Product("Product C", 70.0)
        ]
        shop = Shop(products)
        self.assertEqual(shop.get_most_expensive_product().name, "Product C")

    def test_get_most_expensive_product_empty_shop(self):
        products = []
        shop = Shop(products)
        with self.assertRaises(ValueError):
            shop.get_most_expensive_product()


class TestCalculator(unittest.TestCase):

    def test_calculate_discount(self):
        result = Calculator.calculate_discount(100.0, 20.0)
        self.assertEqual(result, 80.0)

    def test_calculate_discount_invalid_input(self):
        with self.assertRaises(ArithmeticError):
            Calculator.calculate_discount(-100.0, 20.0)

        with self.assertRaises(ArithmeticError):
            Calculator.calculate_discount(100.0, -20.0)

        with self.assertRaises(ArithmeticError):
            Calculator.calculate_discount(100.0, 120.0)


if __name__ == '__main__':
    unittest.main()
