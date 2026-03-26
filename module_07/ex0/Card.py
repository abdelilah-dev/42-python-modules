from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> str:
        ...

    def get_card_info(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}

    def is_playable(self, avaible_mana: int) -> bool:
        if (avaible_mana >= 5):
            self.effect = "Creature summoned to battlefield"
            self.mana_used = 5
            return True
        return False
