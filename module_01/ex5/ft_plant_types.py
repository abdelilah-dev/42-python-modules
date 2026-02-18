class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = "read"
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)
        self.color = "read"
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def produce_shade(self):
        print(f"{self.name} is blooming beautifully!")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

