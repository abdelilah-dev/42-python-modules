from ex0 import Card, CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from typing import List
from random import randint, choice


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        self.cards = [c for c in self.cards if c.name != card_name]

    def shuffle(self) -> None:
        shuffled_cards = []
        for i in self.cards:
            rand_card = choice(self.cards)
            while (rand_card in shuffled_cards):
                rand_card = choice(self.cards)
            shuffled_cards.append(rand_card)
        self.cards = shuffled_cards

    def draw_card(self) -> Card:
        card = self.cards[randint(0, len(self.cards) - 1)]
        print(f"Drew: {card.name}", end=" ")
        if isinstance(card, CreatureCard):
            print("(Creature)")
        elif isinstance(card, SpellCard):
            print("(Spell)")
        elif isinstance(card, ArtifactCard):
            print("(Artifact)")
        return card

    def get_deck_stats(self) -> dict:
        creatures = len([1 for c in self.cards if isinstance(c, CreatureCard)])
        spells = len([1 for c in self.cards if isinstance(c, SpellCard)])
        artifacts = len([1 for c in self.cards if isinstance(c, ArtifactCard)])

        avg_cost = sum([c.cost for c in self.cards]) / len(self.cards)
        return {
            'total_cards': len(self.cards),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
