class Koala:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


def run_week2() -> None:
    koko = Koala("koko", 4)
    koko.greet()
