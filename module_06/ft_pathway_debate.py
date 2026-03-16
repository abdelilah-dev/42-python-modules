import alchemy
from sys import stderr

def pathway_mastery() -> None:
	try:
		print("=== Pathway Debate Mastery ===")

		print("\nTesting Absolute Imports (from basic.py):")
		print(f"lead_to_gold(): {alchemy.lead_to_gold()}")
		print(f"stone_to_gem(): {alchemy.stone_to_gem()}")

		print("\nTesting Relative Imports (from advanced.py):")
		print(f"philosophers_stone(): {alchemy.philosophers_stone()}")
		print(f"elixir_of_life(): {alchemy.elixir_of_life()}")

		print("\nTesting Package Access:")
		print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
		print(f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")

		print("Both pathways work! Absolute: clear, Relative: concise")
	except Exception as error:
		print(error, file=stderr)



if __name__ == "__main__":
	pathway_mastery()
