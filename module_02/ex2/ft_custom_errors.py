class GardenError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.heat_degree = 10
        self.water_in_tank = 5

    def check_heat_degree(self):
        if (self.heat_degree > 30 and not self.water_in_tank):
            raise PlantError(f"The {self.name} plant is wilting!")
        else:
            print("good heat degree and enough water for plant")

    def check_water_in_tank(self):
        if (not self.water_in_tank):
            raise WaterError("Not enough water in the tank!")
        else:
            print("Good enough water in the tank!")


def test_custom_errors():

    tomato = Plant("tomato", 10)

    def create_error(plant: Plant):
        plant.heat_degree = 40
        plant.water_in_tank = 0

    try:
        print("\nTesting PlantError...")
        try:
            create_error(tomato)
            tomato.check_heat_degree()
        except PlantError as error:
            print(f"Caugth PlantError: {error}")

        print("\nTesting WaterError...")
        try:
            create_error(tomato)
            tomato.check_water_in_tank()
        except WaterError as error:
            print(f"Caught WaterError: {error}")

        print("\nTesting catching all garden errors..")

        try:
            create_error(tomato)
            tomato.check_heat_degree()
        except GardenError as error:
            print(f"Caugth PlantError: {error}")

        try:
            create_error(tomato)
            tomato.check_water_in_tank()
        except GardenError as error:
            print(f"Caught WaterError: {error}")

        print("\nAll custom error types work correctly!")
    except Exception as error:
        print(f"Tester Failed: {error}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_custom_errors()
