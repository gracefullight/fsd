class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def eat(self) -> None:
        print(f"{self.name} is eating.")


class Koala(Animal):
    pass


class Kangaroo(Animal):
    def jump(self) -> None:
        print(f"{self.name} is jumping.")


class Bird:
    def make_sound(self) -> None:
        print("Tweet tweet!")


class Emu(Bird):
    def make_sound(self) -> None:
        print("Grunt!")


def speak(bird: Bird) -> None:
    bird.make_sound()


def run_week2() -> None:
    koko = Koala("koko", 4)
    koko.greet()

    kang = Kangaroo("kang", 3)
    kang.greet()
    kang.jump()

    speak(Bird())
    speak(Emu())
