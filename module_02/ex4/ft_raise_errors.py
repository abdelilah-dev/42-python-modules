def check_plant_health(plant_name: str,
                       water_level: int, slight_h: int) -> None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    elif water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        else:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

    elif slight_h < 2 or slight_h > 12:
        if slight_h < 2:
            raise ValueError(f"Sunlight hours {slight_h} is too low (min 2)")
        else:
            raise ValueError(f"Sunlight hours {slight_h} is too high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    try:
        print("\nTesting good values...")
        try:
            check_plant_health("tomato", 5, 4)
        except ValueError as e:
            print(f"Error: {e}")

        print("\nTesting empty plant name...")
        try:
            check_plant_health("", 5, 4)
        except ValueError as e:
            print(f"Error: {e}")

        print("\nTesting bad water level...")
        try:
            check_plant_health("tomato", 12, 7)
        except ValueError as e:
            print(f"Error: {e}")

        print("\nTesting bad sunlight hours...")
        try:
            check_plant_health("tomato", 8, 1)
            print("Plant 'tomato' is healthy!")
        except ValueError as e:
            print(f"Error: {e}")
        print("\nAll error raising tests completed!")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
