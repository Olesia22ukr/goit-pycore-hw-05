#Завдання 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
             return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
print(fib(20))

#Завдання 2
import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    numbers = re.findall(r"\s\d+\.\d+\s", text)
    for num in numbers:
        yield float(num.strip())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
