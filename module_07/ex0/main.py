from .CreatureCard import CreatureCard
from sys import stderr


def test_mana_available(card, mana: int) -> None:
	playable = card.is_playable(mana)
	print(f"Playable: {playable}")
	if playable:
		print(card.play({"name": card.name, "mana_used": card.mana_used, "effect": card.effect}))


def datadeck_card_foundation():
	try:
		print("\n=== DataDeck Card Foundation ===")

		print("\nTesting Abstract Base Class Design:")
		obj = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

		print("\nCreatureCard Info:")
		print(obj.get_card_info())

		print("\nPlaying Fire Dragon with 6 mana available:")
		test_mana_available(obj, 6)

		print("\nFire Dragon attacks Goblin Warrior:")
		attack_res = obj.attack_target("Goblin Warrior")
		print(f"Attack result: {attack_res}")

		print("\nTesting insufficient mana (3 available):")
		test_mana_available(obj, 3)

		print("\nAbstract pattern successfully demonstrated!")
	except Exception as e:
		print(f"Failed to Demonstrate Abstract Pattern: {e}", file=stderr)

if __name__ == "__main__":
	datadeck_card_foundation()
