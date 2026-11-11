# Import the functions we want to test
from project import (
    calculate_average,
    find_highest_rate,
    find_lowest_rate,
    calculate_percentage_change,
    calculate_forecast,
)

def test_calculate_average():
    # The average of 10, 20, and 30 should be 20
    assert calculate_average([10, 20, 30]) == 20


def test_find_highest_rate():
    # The highest value in this list should be 54.95
    assert find_highest_rate([51.73, 54.95, 49.61]) == 54.95


def test_find_lowest_rate():
    # The lowest value in this list should be 49.61
    assert find_lowest_rate([51.73, 54.95, 49.61]) == 49.61


def test_calculate_percentage_change():
    # The rate increases from 50 to 60, which is a 20% increase
    assert calculate_percentage_change(50, 60) == 20


def test_calculate_forecast():
    # The forecast should decrease from 50 to 48
    assert calculate_forecast(50, -2) == 48
