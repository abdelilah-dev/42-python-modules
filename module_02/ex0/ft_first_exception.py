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

def test_temperature_input():
	print("=== Garden Temperature Checker ===")
	test_list = ["30", "abc", "99", "-67"]
	for test in test_list:
		print(f"\nTesting temperature: {test}")
		try:
			check_temperature(test)
		except:
			print(f"Program crashed, test failed at {test}")
			return

	print("\nAll tests completed - program didn't crash!")
	pass

if __name__ == "__main__":
	test_temperature_input()
