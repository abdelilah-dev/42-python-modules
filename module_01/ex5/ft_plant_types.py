class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    classmethod


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = "read"
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, dia: int) -> None:
        super().__init__(name, height, age)
        self.diameter = dia
        print(f"{name} (Tree): {height}cm, {age} days, {dia}cm diameter")

    def produce_shade(self):
        shade: float = 3.1416 * (((self.diameter / 2) * 0.01) ** 2)
        print(f"{self.name} provides {shade:.2f} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, grade: str) -> None:
        super().__init__(name, height, age)
        self.haverst_season = season
        self.natur_value = grade
        print(f"{self.name} (Vegetable): {self.height}cm,", end="")
        print(" {self.age} days, {self.haverst_season} harvest")


    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin {self.natur_value}\n")


def plant_types():
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()

    dak = Tree("Dak", 500, 1825, 50)
    dak.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    tomato.nutritional_value()

    sunflower = Flower("Sunflower", 180, 75, "yellow")
    sunflower.bloom()

    maple = Tree("Maple", 1200, 3650, 900)
    maple.produce_shade()

    cucumber = Vegetable("Cucumber", 40, 70, "summer", "B")
    cucumber.nutritional_value()


if __name__ == "__main__":
    plant_types()
