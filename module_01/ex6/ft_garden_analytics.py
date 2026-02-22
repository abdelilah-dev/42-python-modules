class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self._type = "regular"

    def height_validation(self) -> None:
        if (self.height > 0):
            print("\nHeight validation test: True")
        else:
            print("\nHeight validation test: False")

    def get_type(self) -> str:
        return self._type

    def summary(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self._type = "flowering"

    def summary(self) -> None:
        print(f"- {self.name}: {self.height}cm,",
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize) -> None:
        super().__init__(name, height, color)
        self.prize_point = prize
        self._type = "prize flowers"

    def summary(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.height}",
              f" flowers (blooming), Prize points: {self.prize_point}")


class Garden:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.t_growing = 0
        self.score = score
        self.total_plants: int = 0
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def help_to_grow(self, unit: int) -> None:
        if (unit > 0):
            print(f"\n{self.name} is helping all plants grow...")
            for plant in self.plants:
                plant.height += unit
                self.t_growing += unit
                self.score += 1
                print(f"{plant.name} grew {unit}cm")


class GardenManager:
    gardens: list[Garden] = []
    total_gradens = 0

    def __init__(self) -> None:
        self.state = self.GardenStats()

    @classmethod
    def add_garden(cls, garden: Garden) -> None:
        cls.gardens.append(garden)
        cls.total_gradens += 1

    @staticmethod
    def create_garden_network(garden: Garden,
                              garden_network: list[Plant]) -> None:
        for plant in garden_network:
            garden.add_plant(plant)

    def manager_summary(self) -> None:
        print("Garden scores - ", end="")
        for i in range(self.total_gradens):
            if i != 0:
                print(", ", end="")
            print(f"{self.gardens[i].name}: {self.gardens[i].score}", end="")
        print(f"\nTotal gardens managed: {self.total_gradens}")

    class GardenStats:
        def display_stat(self, garden: Garden) -> None:
            print("\n=== Alice's Garden Report ===")
            self.plants_stat(garden)
            self.statistics(garden)

        def plants_stat(self, garden: Garden) -> None:
            print("Plants in garden:")
            for plant in garden.plants:
                plant.summary()

        @staticmethod
        def statistics(garden: Garden) -> None:
            print(f"\nPlants added: {garden.total_plants},",
                  f"Total growth: {garden.t_growing}cm")
            p_type = []
            for plant in garden.plants:
                p_type.append(plant.get_type())
            print("Plant types: ", end="")
            print(f"{p_type.count("regular")} regular,",
                  f"{p_type.count("flowering")} flowering",
                  f"{p_type.count("prize flowers")} prize flowers")


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
