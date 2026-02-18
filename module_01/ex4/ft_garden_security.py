class SecurePlant:
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        if (height < 0):
            print("\nInvalid operation attempted:", end="")
            print(f" height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age):
        if (age < 0):
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {self.__age}cm [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def state(self):
        print(f"Current plant: {self.name} ({self.__height}cm,", end="")
        print(f" {self.__age} days)")


def main():
    plant = SecurePlant("Rose")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-10)

    plant.state()


if __name__ == "__main__":
    main()
