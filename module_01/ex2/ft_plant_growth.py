class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.init_age = age
        self.added_height = 0

    def grow(self) -> None:
        self.added_height += 1
        self.height += 1

    def age(self) -> None:
        self.init_age += 1

    def get_info(self) -> None:
        print(f"=== Day {i} ===")
        print(f"{self.name}: {self.height}cm", end="")
        print(f", {self.init_age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    plants = [rose, sunflower]

    for plant in plants:
        for i in range(1, 8):
            if i != 1:
                plant.grow()
                plant.age()
            plant.get_info()
        print(f"Growth this week: +{plant.added_height}cm\n")
