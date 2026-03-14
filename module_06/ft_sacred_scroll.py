import alchemy


def direct_module_access():
    try:
        print("\nTesting direct module access:")

        print("alchemy.elements.create_fire(): ", end="")
        try:
            result = alchemy.elements.create_fire()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

        print("alchemy.elements.create_water(): ", end="")
        try:
            result = alchemy.elements.create_water()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

        print("alchemy.elements.create_earth(): ", end="")
        try:
            result = alchemy.elements.create_earth()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

        print("alchemy.elements.create_air(): ", end="")
        try:
            result = alchemy.elements.create_air()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

    except OSError as error:
        print(f"Direct Module Accessing Problem: {error}")


def package_level_access():
    try:
        print("\nTesting package-level access (controlled by __init__.py):")

        print("alchemy.create_fire(): ", end="")
        try:
            result = alchemy.create_fire()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

        print("alchemy.create_water(): ", end="")
        try:
            result = alchemy.create_water()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

        print("alchemy.create_earth(): ", end="")
        try:
            result = alchemy.create_earth()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)

        print("alchemy.create_air(): ", end="")
        try:
            result = alchemy.create_air()
        except AttributeError:
            result = "AttributeError - not exposed"
        print(result)
    except OSError as error:
        print(f"Package Level Accessing Problem: {error}")


def package_metadata():
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    direct_module_access()
    package_level_access()
    package_metadata()
