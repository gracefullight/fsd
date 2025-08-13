import math

x = 4
y = 2


def add(x: int, y: int) -> None:
    print(x + y)


def subtract(x: int, y: int) -> None:
    print(x - y)


def multiply(x: int, y: int) -> None:
    print(f"{x * y:.2f}")


def divide(x: int, y: int) -> None:
    print(f"{x / y:.2f}")


def modules_plus_divide(x: int, y: int) -> None:
    print(f"{x % y + x / y:.2f}")


def high_order(x: int, y: int) -> None:
    answer = (y**7 + 7 / (math.sqrt(5) + x)) * (x**4 % 5 + 2)
    print(f"{answer:.2f}")


add(x, y)
subtract(x, y)
multiply(x, y)
divide(x, y)
modules_plus_divide(x, y)
high_order(x, y)
