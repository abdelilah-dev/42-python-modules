import alchemy.elements
import alchemy.potions
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water


def importing_methods() -> None:
    try:
        print("\nMethod 1 - Full module import:")
        print("alchemy.elements.create_fire(): ", end="")
        try:
            result = alchemy.elements.create_fire()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

        print("\nMethod 2 - Specific function import:")
        print(f"create_water(): {create_water()}")

        print("\nMethod 3 - Aliased import:")
        print(f"heal(): {heal()}")

        print("\nMethod 4 - Multiple imports:")
        print(f"create_earth(): { alchemy.elements.create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {alchemy.potions.strength_potion()}")

        print("\nAll import transmutation methods mastered!")
    except OSError as error:
        print(f"Failed Importing Methods - {error}")


if __name__ == "__main__":
    importing_methods()
