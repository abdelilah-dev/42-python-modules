class Player:
    def __init__(self, name: str, score: int, achiv: str,
                 active: bool, region: str) -> None:
        self.name = name
        self.score = score
        self.achiv = achiv.split(",")
        self.active = active
        self.region = region


class Players:
    def __init__(self) -> None:
        self.players = list()

    def add_player(self, player: Player) -> None:
        if not player.name:
            raise ValueError("Player Name Can't Be Empty")
        else:
            self.players.append(player)


def list_comprehension(pl_manager: Players) -> None:
    try:
        print("=== List Comprehension Examples ===")
        print("High scorers (>2000):",
              f"{[x.name for x in pl_manager.players if x.score > 2000]}")
        print(f"Scores doubled: {[x.score * 2 for x in pl_manager.players]}")
        print("Active players:",
              f"{[pl.name for pl in pl_manager.players if pl.active]}")
    except Exception as error:
        print(f"Error in List Comprehension: {error}")


def dict_comprehension(pl_manager: Players) -> None:
    print("\n=== Dict Comprehension Examples ===")
    try:
        x = {pl.name: pl.score for pl in pl_manager.players}
        print(f"Player scores: {x}")

        all_scores = [pl.score for pl in pl_manager.players]
        high = len({sc for sc in all_scores if sc > 2100})
        medium = len({sc for sc in all_scores if sc > 2000 and sc < 2100})
        low = len({sc for sc in all_scores if sc < 2000})
        sc_categories = {'high': high, 'medium': medium, 'low': low}
        print(f"Score categories: {sc_categories}")

        ach_count = {pl.name: len(pl.achiv) for pl in pl_manager.players}
        print(f"Achievement counts: {ach_count}")
    except Exception as error:
        print(f"Error in Dict Comprehension: {error}")


def set_comprehension(pl_manger: Players) -> None:
    try:
        print("\n=== Set Comprehension Examples ===")
        unique_pl = {pl.name for pl in pl_manger.players}
        print(f"Unique players: {unique_pl}")

        unique_achiv = {achiv for pl in pl_manger.players
                        for achiv in pl.achiv}
        print(f"Unique achievements: {unique_achiv}")

        active_region = {pl.region for pl in pl_manger.players if pl.active}
        print(f"Active regions: {active_region}")
    except Exception as error:
        print(f"Error in Set Comprehension: {error}")


def combined_analysis(pl_manger: Players) -> None:
    print("\n=== Combined Analysis ===")
    try:
        print(f"Total players: {len(p_manager.players)}")
        print("Total unique achievements:",
              f"{len({ach for row in p_manager.players
                      for ach in row.achiv})}")

        total_score = sum([pl.score for pl in p_manager.players])
        print(f"Average score: {total_score / len(p_manager.players)}")

        finall_sc = {pl.name: pl.score + (len(pl.achiv) * 50)
                     for pl in p_manager.players}
        finall_sc = sorted(finall_sc.items(), key=lambda item: item[1],
                           reverse=True)[0]
        winner = [pl for pl in p_manager.players if pl.name == finall_sc[0]]
        print(f"Top performer: {winner[0].name}",
              f"({winner[0].score} points,",
              f"{len(winner[0].achiv)} achievements)")
    except Exception as error:
        print(f"Error in Combination Analysis: {error}")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    try:
        p_manager = Players()

        achiv = "first_kill,level_10,treasure_hunter,speed_demon"
        alice = Player("alice", 2300, achiv, True, "north")

        achiv = "treasure_hunter,speed_demon"
        charlie = Player("charlie", 2150, achiv, True, "east")

        achiv = "boss_slayer,collector"
        bob = Player("bob", 1800, achiv, True, "central")

        achiv = "treasure_hunter,collector"
        diana = Player("diana", 2050, achiv, False, "Hidden")

        p_manager.add_player(alice)
        p_manager.add_player(charlie)
        p_manager.add_player(bob)
        p_manager.add_player(diana)

        list_comprehension(p_manager)

        dict_comprehension(p_manager)

        set_comprehension(p_manager)

        combined_analysis(p_manager)
    except Exception as error:
        print(error)
