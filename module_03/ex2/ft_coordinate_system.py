import math
import sys

def create_positions(cordinates: list[str | int]) -> tuple:
    position: tuple = ()
    for pos in cordinates:
        position += (int(pos),)
    return position

def calculate_distance(f: tuple, t: tuple) -> None:
    return (math.sqrt((t[0]-f[0])**2 + (t[1]-f[1])**2 + (t[2]-f[2])**2))

def parse_position(fr: str, to: str | tuple):
    try:
        from_pos = create_positions(fr.split(","))
        to_pos = create_positions(to.split(","))
        print(f"Parsed position: {to}")
        print(f"Distance between {from_pos} and {to_pos} : {calculate_distance(from_pos, to_pos):.2f}")
    except Exception as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error.args}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    try:
        coordinate = (10, 20, 5)
        print(f"\nPosition created: {coordinate}")
        print(f"Distance between (0, 0, 0) and {coordinate}: {calculate_distance((0, 0, 0), coordinate):.2f}")

        print(f"\nParsing coordinates: \"3,4,0\"")
        parse_position("0,0,0", coordinate)

        print(f"\nParsing invalid coordinates: \"abc,def,ghi\"")
        parse_position("0,0,0", "abc,def,ghi")

        print("Unpacking demonstration:")
        x, y, z = coordinate
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except Exception as error:
        print(error)


