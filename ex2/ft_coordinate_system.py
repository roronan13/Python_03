#!usr/bin/env python3

import math


def get_player_pos() -> tuple:
    while True:
        user_input: str = input("Enter new coordinates as \
floats in format 'x,y,z' : ")
        coordinates_str: list[str] = user_input.split(',')

        try:
            if len(coordinates_str) != 3:
                raise ValueError("Invalid syntax\n")
        except ValueError as e:
            print(f"{e}")
            continue

        coordinates: list[float] = []
        for value_str in coordinates_str:
            try:
                coordinates.append(float(value_str))
            except ValueError as e:
                print(f"Error on parameter '{value_str}' : {e}\n")
                break
        else:
            return tuple(coordinates)


if __name__ == "__main__":
    print(" === Game coordinate system === \n")

    print("Get a first set of coordinates")
    first_tuple: tuple = get_player_pos()
    print(f"Got a first tuple : {first_tuple}")
    print(f"It includes : X={first_tuple[0]}, Y={first_tuple[1]}, \
Z={first_tuple[2]}")
    print(f"Distance to the center : {round(math.sqrt((first_tuple[0])**2 +
                                            (first_tuple[1])**2 +
                                            (first_tuple[2])**2), 4)}")

    print("\nGet a second set of coordinates")
    second_tuple: tuple = get_player_pos()
    print(f"Distance between the two sets \
of coordinates : {round(math.sqrt((first_tuple[0] - second_tuple[0])**2 +
                                  (first_tuple[1] - second_tuple[1])**2 +
                                  (first_tuple[2] - second_tuple[2])**2), 4)}")
