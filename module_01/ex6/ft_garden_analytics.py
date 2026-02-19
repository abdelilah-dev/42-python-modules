class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.__type = "regular"

    def height_validation(self) -> None:
        if (self.height > 0):
            print("Height validation test: True")
        else:
            print("Height validation test: False")

    def get_type(self) -> str:
        return self.__type

    def summary(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.__type = "flowering"

    def get_type(self) -> str:
        return self.__type

    def summary(self) -> None:
        print(f"- {self.name}: {self.height}cm,",
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize) -> None:
        super().__init__(name, height, color)
        self.prize_point = prize
        self.__type = "prize flowers"

    def get_type(self) -> str:
        return self.__type

    def summary(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.height}",
              f" flowers (blooming), Prize points: {self.prize_point}")


class Garden:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.t_growing = 0
        self.score = score
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def help_to_grow(self, unit: int) -> None:
        if (unit > 0):
            print(f"{self.name} is helping all plants grow...")
            i = 0
            while i < len(self.plants):
                self.plants[i].height += unit
                self.t_growing += unit
                self.score += 1
                print(f"{self.plants[i].name} grew {unit}cm")
                i += 1


class GardenManager:
    gardens: list[Garden] = []

    def __init__(self) -> None:
        self.state = self.GardenStats()

    @classmethod
    def add_garden(cls, garden: Garden) -> None:
        cls.gardens.append(garden)

    @staticmethod
    def create_garden_network(garden: Garden,
                              garden_network: list[Plant]) -> None:
        i = 0
        while i < len(garden_network):
            garden.add_plant(garden_network[i])
            i += 1

    def manager_summary(self) -> None:
        print("Garden scores - ", end="")
        for i in range(len(self.gardens)):
            if i != 0:
                print(", ", end="")
            print(f"{self.gardens[i].name}: {self.gardens[i].score}", end="")
        print(f"\nTotal gardens managed: {len(self.gardens)}")

    class GardenStats:
        def display_stat(self, garden: Garden) -> None:
            print("\n=== Alice's Garden Report ===\n")
            self.plants_stat(garden)
            self.statistics(garden)

        def plants_stat(self, garden: Garden) -> None:
            print("Plants in garden:")
            i = 0
            while i < len(garden.plants):
                garden.plants[i].summary()
                i += 1

        @staticmethod
        def statistics(garden: Garden) -> None:
            print(f"Plants added: {len(garden.plants)},",
                  f"Total growth: {garden.t_growing}cm")
            p_type = []
            i = 0
            while i < len(garden.plants):
                p_type.append(garden.plants[i].get_type())
                i += 1
            i = 0
            print("Plant types: ", end="")
            while i < len(garden.plants):
                if (i):
                    print(", ", end="")
                print(f"{p_type.count(garden.plants[i].get_type())}",
                      f" {garden.plants[i].get_type()}", end="")
                if (i == len(garden.plants) - 1):
                    print("\n", end="")
                i += 1


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    garden_manager = GardenManager()

    alice = Garden("Alice", 203)
    bob = Garden("Bob", 96)

    garden_manager.add_garden(alice)
    garden_manager.add_garden(bob)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_network = [oak, rose, sunflower]

    garden_manager.create_garden_network(alice, alice_network)
    alice.help_to_grow(1)

    garden_manager.state.display_stat(alice)

    alice.plants[0].height_validation()

    garden_manager.manager_summary()


if __name__ == "__main__":
    main()
