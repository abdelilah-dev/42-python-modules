class GardenError(Exception):
	def __init__(self, name: str, *args: object) -> None:
		self.name = name
		super().__init__(f"Caught PlantError: The {self.name} plant is wilting!")


class PlantError(GardenError):
	def __init__(self, *args: object) -> None:
		super().__init__(*args)

class WaterError(GardenError):
	def __init__(self, *args: object) -> None:
		super().__init__(*args)

if __name__ == "__main__":
	Plant = GardenError()
	try:
		print("Testing PlantError...")
		raise PlantError("tomato")
	except PlantError as e:
		print(e)


