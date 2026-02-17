class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    obj_one = Plant("Rose", 25, 30)
    obj_two = Plant("Sunflower", 80, 45)
    obj_three = Plant("Cactus", 15, 120)
    all_o = [obj_one, obj_two, obj_three]

    print("=== Garden Plant Registry ===")
    for i in range(3):
        print(f"{all_o[i].name}: {all_o[i].height}cm, {all_o[i].age} days old")

