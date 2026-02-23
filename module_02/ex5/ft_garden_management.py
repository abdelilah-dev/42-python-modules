class WaterError(Exception):
    def __init__(self, msg: str) -> None:
        self.message = msg
        super().__init__(self.message)


class HealthError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg
        super().__init__(self.msg)


class GardenError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg
        super().__init__(f"Caught GardenError: {self.msg}")


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.water_in_tank = 2

    def add_plant(self, plant: Plant) -> None:
        try:
            if not plant.name:
                raise ValueError("Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except Exception as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if (self.water_in_tank <= 0):
                    raise GardenError("Not enough water in the tank!")
                if not plant.name:
                    raise WaterError("Cannot water None - invalid plant!")
                else:
                    print(f"Watering {plant.name} - success")
                    plant.water += 1
                    self.water_in_tank -= 1
            print("Watering completed successfully")
        except (WaterError, GardenError) as error:
            print(error)
            raise WaterError("Watering doesn't completed successfully")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        water = plant.water
        sun = plant.sun
        if water < 1 or water > 10:
            if water < 1:
                raise HealthError(f"Water level {water} is too low (min 1)")
            else:
                raise HealthError(f"Water level {water} is too high (max 10)")

        elif sun < 2 or sun > 12:
            if sun < 2:
                raise HealthError(f"Sunlight hours {sun} is too low (min 2)")
            else:
                raise HealthError(f"Sunlight hours {sun} is too high (max 12)")
        print(f"{plant.name}: healthy",
              f"(water: {plant.water}, sun: {plant.sun})")

    def check_water_in_tank(self) -> None:
        if self.water_in_tank <= 0:
            raise GardenError("Not enough water in the tank!")
        else:
            print("Good enough water in the tank!")


def test_garden_management() -> None:
    garden_manager = GardenManager()

    try:
        tomato = Plant("tomato", 5, 8)
        lettuce = Plant("lettuce", 14, 6)
        rose = Plant("", 10, 4)

        print("\nAdding plants to garden...")
        garden_manager.add_plant(tomato)
        garden_manager.add_plant(lettuce)
        garden_manager.add_plant(rose)

        print("\nWatering plants...")
        garden_manager.water_plants()

        print("\nChecking plant health...")
        for plant in garden_manager.plants:
            try:
                garden_manager.check_plant_health(plant)
            except HealthError as error:
                print(f"Error checking {plant.name}: {error}")

        print("\nTesting error recovery...")
        try:
            garden_manager.check_water_in_tank()
        except GardenError as error:
            print(error)
        finally:
            print("System recovered and continuing...")

    except Exception as error:
        print(error)
    finally:
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    test_garden_management()
