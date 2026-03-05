import math
import sys


def create_positions(cordinates: list[str | int]) -> tuple:
    position: tuple = ()
    for pos in cordinates:
        position += (int(pos),)
    return position


def calculate_distance(f: tuple, t: tuple) -> None:
    return (math.sqrt((t[0]-f[0])**2 + (t[1]-f[1])**2 + (t[2]-f[2])**2))


def parse_position(pos: str) -> tuple:
    try:
        coordinate = create_positions(pos.split(","))
        print(f"Parsed position: {coordinate}")
        return coordinate
    except Exception as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error.args}")


def display_distance(home: tuple, coordinate: tuple) -> None:
    try:
        if coordinate and home:
            print(f"Distance between {home} and {coordinate}:",
                  f"{calculate_distance(home, coordinate):.2f}")
        else:
            raise ValueError("Positions can't be None!")
    except Exception as error:
        print(f"Error When Try to Display Distance: {error}")


def unpacking_demonstration(coordinate: tuple) -> None:
    print("\nUnpacking demonstration:")
    x, y, z = coordinate
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    try:
        home = (0, 0, 0)
        coordinate = (10, 20, 5)
        print(f"\nPosition created: {coordinate}")
        display_distance(home, coordinate)

        print("\nParsing coordinates: \"3,4,0\"")
        coordinate = parse_position("3,4,0")
        display_distance(home, coordinate)

        print("\nParsing invalid coordinates: \"abc,def,ghi\"")
        coordinate = parse_position("abc,def,ghi")
        display_distance(home, coordinate)

        coordinate = (3, 4, 0)
        unpacking_demonstration(coordinate)

        if len(sys.argv) > 1:
            i = 1
            while i < len(sys.argv):
                print(f"\nParse Your Coordinates: {sys.argv[i]}")
                coordinate = parse_position(sys.argv[i])
                if coordinate is not None:
                    display_distance(home, coordinate)
                i += 1
    except Exception as error:
        print(error)
