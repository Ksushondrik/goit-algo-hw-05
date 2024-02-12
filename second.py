import re
from typing import Callable


def generator_numbers(some_text: str):
    for match in re.finditer(r'\d+\.\d*', some_text):
        yield float(match.group())


def sum_profit(some_text: str, func: Callable):
    total_sum = 0

    for number in func(some_text):
        total_sum += number

    return total_sum

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
