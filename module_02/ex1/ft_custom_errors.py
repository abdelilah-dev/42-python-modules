def garden_operations() -> None:
	print("=== Garden Error Types Demo ===")
	try:
		print("\nTesting ValueError...")
		value = int("abc")
	except ValueError:
		print("Caught ValueError: invalid literal for int()")

	try:
		print("\nTesting ZeroDivisionError...")
		value = 10 / 0
	except ZeroDivisionError:
		print("Caught ZeroDivisionError: division by zero")

	try:
		print("\nTesting FileNotFoundError...")
		file = open("missing.txt", 'r')
	except FileNotFoundError:
		print("Caught FileNotFoundError: No such file 'missing.txt'")

	try:
		print("\nTesting KeyError...")
		ages = {'alex': 25, 'johan': 20}
		print(ages['bob'])
	except KeyError:
		print("Caught KeyError: 'missing bob'")

	try:
		print("\nTesting multiple errors together...")
		value = int("abc")
		value = 10 / 0
		file = open("missing.txt", 'r')
		ages = {'alex': 25, 'johan': 20}
		ages['bob'] = 40
	except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
		print("Caught an error, but program continues!")

def test_error_types() -> None:
	garden_operations()


if __name__ == "__main__":
	garden_operations()
