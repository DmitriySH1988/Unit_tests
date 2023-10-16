import pytest
from average_calculator import AverageCalculator, compare_averages

def test_compare_averages_first_list_bigger():
    result = compare_averages([2, 3, 4], [1, 1, 1])
    assert result == "Первый список имеет большее среднее значение"

def test_compare_averages_second_list_bigger():
    result = compare_averages([1, 1, 1], [2, 3, 4])
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    result = compare_averages([1, 2, 3], [3, 2, 1])
    assert result == "Средние значения равны"

def test_average_calculator_empty_list():
    calculator = AverageCalculator()
    result = calculator.calculate_average([])
    assert result == 0


# Проверка качества кода с использованием pylint:
# pylint average_calculator.py

# Генерация отчета о покрытии кода тестами с использованием pytest-cov:
# pytest --cov=average_calculator