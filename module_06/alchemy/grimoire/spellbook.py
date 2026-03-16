from .validator import validate_ingredients

def record_spell(spell_name: str, ingredients: str) -> str:
	validation_res = validate_ingredients(ingredients)
	if (validation_res.split(" ")[-1] == "VALID"):
		return f"Spell recorded: {spell_name} ({validation_res})"
	return f"Spell rejected: {spell_name} ({validation_res})"
