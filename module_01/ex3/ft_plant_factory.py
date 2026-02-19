class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    p_one = Plant("Rose", 25, 30)
    p_two = Plant("Dak", 200, 365)
    p_three = Plant("Cactus", 5, 90)
    p_four = Plant("Sunflower", 80, 45)
    p_five = Plant("Fern", 15, 120)
    all_plant: list[Plant] = [p_one, p_two, p_three, p_four, p_five]
    i = 0

    print("=== Plant Factory Output ===")
    while i in range(len(all_plant)):
        print(all_plant[i])
        i += 1

    print(f"\nTotal plants created: {len(all_plant)}")


if __name__ == "__main__":
    main()
