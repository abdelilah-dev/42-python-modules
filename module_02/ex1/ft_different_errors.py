def garden_operations(operation_type: str) -> None:
    if operation_type == "ValueError":
        _ = int("abc")

    elif operation_type == "ZeroDivisionError":
        _ = 10 / 0

    elif operation_type == "FileNotFoundError":
        _ = open("missing.txt", 'r')

    elif operation_type == "KeyError":
        ages = {'alex': 25, 'johan': 20}
        print(ages['bob'])

    elif operation_type == "multi":
        _ = int("abc")
        _ = 10 / 0
        _ = open("missing.txt", 'r')
        ages = {'alex': 25, 'johan': 20}
        ages['bob'] = 40


def test_error_types() -> None:
    try:
        print("\nTesting ValueError...")
        try:
            garden_operations("ValueError")
        except ValueError:
            print("Caught ValueError: invalid literal for int()")

        print("\nTesting ZeroDivisionError...")
        try:
            garden_operations("ZeroDivisionError")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")

        print("\nTesting FileNotFoundError...")
        try:
            garden_operations("FileNotFoundError")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")

        print("\nTesting KeyError...")
        try:
            garden_operations("KeyError")
        except KeyError:
            print("Caught KeyError: 'missing bob'")

        print("\nTesting multiple errors together...")
        try:
            garden_operations("multi")
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")
        print("\nAll error types tested successfully!")
    except Exception as e:
        print(f"Error Types Tester Failed : {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
