class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.init_age = age
        self.added_height = 0

    def grow(self, growing_height: int) -> None:
        self.added_height += growing_height
        self.height += self.added_height

    def age(self) -> None:
        self.init_age += 6

    def get_info(self, growing_height: int) -> None:
        rose.grow(growing_height)
        rose.age()
        print("=== Day 1 ===")
        print(f"{self.name}: {self.height - self.added_height}cm", end="")
        print(f", {self.init_age - 6} days old")
        print("=== Day 7 ===")
        print(f"{self.name}: {self.height}cm, {self.init_age} days old")
        print(f"Growth this week: +{self.added_height}cm")


if __name__ == "__main__":
    """
        In the get_info method, I added a parameter that
        represents the growing height for this week.
    """
    rose = Plant("Rose", 25, 30)
    rose.get_info(8)
