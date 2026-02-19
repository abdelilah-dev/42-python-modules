class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant_one = Plant("Rose", 25, 30)
    plant_two = Plant("Sunflower", 80, 45)
    plant_three = Plant("Cactus", 15, 120)
    plants = [plant_one, plant_two, plant_three]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant)
