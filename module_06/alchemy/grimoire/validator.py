
def validate_ingredients(ingredients: str) -> str:
	valid = ["fire", "water", "earth", "air"]
	for ele in ingredients.split(" "):
		if ele in valid:
			return f"{ingredients} VALID"
	return f"{ingredients} INVALID"
