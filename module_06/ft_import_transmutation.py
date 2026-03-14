import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water, create_earth


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
        print(f"create_earth(): { create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strenght_potion()}")

    except OSError as error:
        print("")


if __name__ == "__main__":
    importing_methods()
    pass
