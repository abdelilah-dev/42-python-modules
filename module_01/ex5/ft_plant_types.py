class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = "read"

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, ",
              f"{self.age} days, {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, dia: int) -> None:
        super().__init__(name, height, age)
        self.diameter = dia

    def produce_shade(self) -> None:
        shade: float = 3.1416 * (((self.diameter / 2) * 0.01) ** 2)
        print(f"{self.name} provides {shade:.2f} square meters of shade")

    def get_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, ",
              f"{self.age} days, {self.diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, grade: str) -> None:
        super().__init__(name, height, age)
        self.haverst_season = season
        self.natur_value = grade

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm,",
              f" {self.age} days, {self.haverst_season} harvest",
              f"{self.name} is rich in vitamin {self.natur_value}")


def plant_types() -> None:
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.get_info()

    dak = Tree("Dak", 500, 1825, 50)
    dak.get_info

    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    tomato.get_info()

    sunflower = Flower("Sunflower", 180, 75, "yellow")
    sunflower.get_info()

    maple = Tree("Maple", 1200, 3650, 900)
    maple.get_info()

    cucumber = Vegetable("Cucumber", 40, 70, "summer", "B")
    cucumber.get_info()


if __name__ == "__main__":
    plant_types()
