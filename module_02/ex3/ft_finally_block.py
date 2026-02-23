class WaterError(Exception):
    def __init__(self, msg: str) -> None:
        self.message = msg
        super().__init__(self.message)


def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for name in plant_list:
            if not name:
                raise WaterError("Cannot water None - invalid plant!")
            else:
                print(f"Watering {name}")
    except WaterError as error:
        print(f"Error: {error}")
        raise WaterError("Watering doesn't completed successfully")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    try:
        good_plant = ["tomato", "lettuce", "carrots"]
        print("\nTesting normal watering...")
        try:
            water_plants(good_plant)
            print("Watering completed successfully!")
        except WaterError as error:
            print(error)

        bad_plant = ["tomato", ""]
        print("\nTesting with error...")
        try:
            water_plants(bad_plant)
            print("Watering completed successfully!")
        except WaterError as error:
            print(error)

    except Exception as error:
        print(f"Tester Failed: {error}")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
