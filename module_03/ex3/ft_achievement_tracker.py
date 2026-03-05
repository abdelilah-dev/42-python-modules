
class Player:
    def __init__(self, name: str, achivement: str = "new_player") -> None:
        self.name = name
        self.achivement = set(achivement.split(","))

    def add_achivement(self, achiv: str) -> None:
        self.achivement = self.achivement | set(achiv.split(","))


class Players:
    def __init__(self) -> None:
        self.players: list[Player] = []
        self.total_players = 0

    def add_player(self, player: Player) -> None:
        try:
            if not player.name:
                raise ValueError("Player Name can't be empty !!\n")
            self.players.append(player)
            self.total_players += 1
        except ValueError as error:
            print(f"Failed To Add Player: {error}")

    def display_players_achievements(self) -> None:
        for player in self.players:
            print(f"Player {player.name} achievements: {player.achivement}")

    def get_unique_achivements(self) -> set:
        unique_achiv = self.players[0].achivement
        for player in self.players:
            unique_achiv = unique_achiv.union(player.achivement)
        return unique_achiv

    def get_common_ele(self) -> set:
        common_ele = self.players[0].achivement
        for player in self.players:
            common_ele = common_ele.intersection(player.achivement)
        return common_ele

    @staticmethod
    def compare_two_players(p1: Player, p2: Player) -> None:
        print(f"{p1.name} vs {p2.name} common:",
              f"{p1.achivement.intersection(p2.achivement)}")
        print(f"{p1.name} unique: {p1.achivement.difference(p2.achivement)}")
        print(f"{p2.name} unique: {p2.achivement.difference(p1.achivement)}")

    def get_rare_achievements(self) -> set:
        rare_achiv: set = set()
        for player in self.players:
            common_ele: set = player.achivement
            for cmp_player in self.players:
                if (cmp_player.name == player.name):
                    continue
                diff = player.achivement.difference(cmp_player.achivement)
                common_ele = common_ele.intersection(diff)
            if not rare_achiv:
                rare_achiv = common_ele
            else:
                rare_achiv = rare_achiv.union(common_ele)
        return (rare_achiv)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    try:
        players = Players()

        ach = "first_kill,level_10,treasure_hunter,speed_demon"
        alice = Player("alice", ach)

        bob = Player("bob", "first_kill,level_10,boss_slayer,collector")

        ach = "level_10,treasure_hunter,boss_slayer,speed_demon,perfectionist"
        charlie = Player("charlie", ach)

        players.add_player(alice)
        players.add_player(bob)
        players.add_player(charlie)

        players.display_players_achievements()

        print("\n=== Achievement Analytics ===")
        unique_achiv = players.get_unique_achivements()
        print(f"All unique achievements: {unique_achiv}")
        print(f"Total unique achievements: {len(unique_achiv)}\n")

        common_ele = players.get_common_ele()
        print(f"Common to all players: {common_ele}")

        rare_achiv = players.get_rare_achievements()
        print(f"Rare achievements (1 player): {rare_achiv}\n")

        players.compare_two_players(alice, bob)
    except Exception as error:
        print(error)
