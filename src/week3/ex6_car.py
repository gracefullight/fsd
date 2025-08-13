class Car:
    def __init__(self, make: str, pos: int) -> None:
        self.make = make
        self.position = pos

    def move(self, dx: int) -> None:
        self.position += dx

    def __str__(self) -> str:
        """Return a string representation of the car's make and position."""
        return f"{self.make} is at position {self.position}"


bmw = Car("BMW", 0)
print(bmw)
bmw.move(5)
print(bmw)
