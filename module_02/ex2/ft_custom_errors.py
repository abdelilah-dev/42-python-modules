class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caugth GardenError: {self.message}"


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caugth PlantError: {self.message}"


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caugth WaterError: {self.message}"


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.heat_degree: int = 10
        self.water_in_tank: int = 5

    def check_wilting_stat(self) -> None:
        if (self.heat_degree > 30 and not self.water_in_tank):
            raise PlantError(f"The {self.name} plant is wilting!")
        else:
            print("good heat degree and enough water for plant")

    def check_water_in_tank(self) -> None:
        if (not self.water_in_tank):
            raise WaterError("Not enough water in the tank!")
        else:
            print("Good enough water in the tank!")


def test_custom_errors() -> None:

    tomato = Plant("tomato", 10)

    def create_error(plant: Plant) -> None:
        plant.heat_degree = 40
        plant.water_in_tank = 0

    try:
        print("\nTesting PlantError...")
        try:
            create_error(tomato)
            tomato.check_wilting_stat()
        except PlantError as error:
            print(error)

        print("\nTesting WaterError...")
        try:
            create_error(tomato)
            tomato.check_water_in_tank()
        except WaterError as error:
            print(error)

        print("\nTesting catching all garden errors..")

        try:
            create_error(tomato)
            tomato.check_wilting_stat()
        except GardenError as error:
            print(error)

        try:
            create_error(tomato)
            tomato.check_water_in_tank()
        except GardenError as error:
            print(error)

        print("\nAll custom error types work correctly!")
    except Exception as error:
        print(f"Tester Failed: {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
