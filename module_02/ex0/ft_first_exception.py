def check_temperature(temp_str: str) -> None:
    try:
        value = int(temp_str)
        if value < 0:
            print(f"Error: {value}°C is too cold for plants (min 0°C)")
        elif value > 40:
            print(f"Error: {value}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {value}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    test_list = ["30", "abc", "99", "-67", None]
    try:
        for test in test_list:
            print(f"\nTesting temperature: {test}")
            check_temperature(test)
        print("\nAll tests completed - program didn't crash!")
    except Exception as e:
        print(f"Checker Failed: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
