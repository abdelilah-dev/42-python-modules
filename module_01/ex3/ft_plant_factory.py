class Plant:
    counter = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.counter += 1

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    p_one = Plant("Rose", 25, 30)
    p_two = Plant("Dak", 200, 365)
    p_three = Plant("Cactus", 5, 90)
    p_four = Plant("Sunflower", 80, 45)
    p_five = Plant("Fern", 15, 120)
    all_plant: list[Plant] = [p_one, p_two, p_three, p_four, p_five]

    print("=== Plant Factory Output ===")
    for plant in all_plant:
        print(plant)

    print(f"\nTotal plants created: {Plant.counter}")


if __name__ == "__main__":
    main()
