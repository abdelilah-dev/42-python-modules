def check_temperature(temp_str: str) -> None:
	print(f"\nTesting temperature: {temp_str}")
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

def test_temperature_input():
	print("=== Garden Temperature Checker ===")
	check_temperature("30")
	check_temperature("abc")
	check_temperature("99")
	check_temperature("-67")
	print("\nAll tests completed - program didn't crash!")
	pass

if __name__ == "__main__":
	test_temperature_input()
