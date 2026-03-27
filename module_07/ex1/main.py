from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from .Deck import Deck
from ex0 import CreatureCard
from sys import stderr


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Deck Builder ===\n")
        creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        artifact = ArtifactCard("Mana Crysta", 3, "Legendary", 6, 4)
        spell = SpellCard("Lightning Bolt", 4, "Lightning Bolt", "damage")

        all_cards = [creature, artifact, spell]

        print("Building deck with different card types...")
        deck_management = Deck()
        for card in all_cards:
            deck_management.add_card(card)

        print(f"Deck stats: {deck_management.get_deck_stats()}")

        print("\nDrawing and playing cards:\n")

        i = 0
        while (i < 3):
            deck_management.shuffle()
            drew_card = deck_management.draw_card()
            print(f"Play result: {drew_card.play(None)}\n")
            i += 1

        print("Polymorphism in action: Same interface,",
              "different card behaviors!")
    except Exception as e:
        print(e, file=stderr)
