from .CreatureCard import CreatureCard
from sys import stderr


def try_play_card(card, mana: int) -> None:
    playable = card.is_playable(mana)
    print(f"Playable: {playable}")
    if playable:
        print(f"Play result: {card.play(None)}")


def run_card_demo():
    try:
        print("\n=== DataDeck Card Foundation ===")

        print("\nTesting Abstract Base Class Design:")

        try:
            card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        except ValueError as e:
            print(f"Failed to Create Card: {e}")

        mana = 6

        print("\nCreatureCard Info:")
        print(card.get_card_info())

        print(f"\nPlaying Fire Dragon with {mana} mana available:")
        try_play_card(card, mana)

        print("\nFire Dragon attacks Goblin Warrior:")
        attack_result = card.attack_target("Goblin Warrior")
        print(f"Attack result: {attack_result}")

        mana = 3
        print(f"\nTesting insufficient mana ({mana} available):")
        try_play_card(card, mana)

        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"Failed to Demonstrate Abstract Pattern: {e}", file=stderr)


if __name__ == "__main__":
    run_card_demo()
