class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, age):
        self.height += age

    def grow_age(self, days):
        self.age += days - 1

    def get_info(self, growing: list[list[int]]):
        total_height_growing = 0
        for i in range(len(growing)):
            print(f"=== Day {growing[i][1]} ===")
            self.grow(growing[i][0])
            self.grow_age(growing[i][1])
            total_height_growing += growing[i][0];
            print(f"{self.name}: {self.height}cm, {self.age} days old")
        if (growing[-1][1] <= 7):
            print(f"Growth this week: +{total_height_growing}cm")
        else:
            print(f"Growth in {growing[len(growing) - 1][1]} Days: +{total_height_growing}cm")

if __name__ == "__main__":
    """

    """
    obj = Plant("Rose", 25, 30)
    growing = [[0, 1], [6, 7]]
    obj.get_info(growing)
