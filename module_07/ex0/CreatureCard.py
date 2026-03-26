from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> str:
        return f"Play result: {game_state}"

    def attack_target(self, target) -> dict:
        return {"attacker": self.name, "target": target,
                "damage_dealt": self.attack, "combat_resolved": True}
