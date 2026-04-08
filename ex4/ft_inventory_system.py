#!usr/bin/env python3

import sys


class DoublonError(Exception):
    def __init__(self, error_message: str):
        super().__init__(error_message)


if __name__ == "__main__":
    print(" === Inventory System Analysis === \n")

    if len(sys.argv) == 1:
        print("No item provided. Command line must be : python3 \
ft_inventory_system.py item_name:quantity item_name:quantity\n")
        sys.exit

    i: int = 1
    item_and_value: list[str]
    inventory: dict = {}

    for i in range(i, len(sys.argv)):
        item_and_value = sys.argv[i].split(':')

        if len(item_and_value) != 2:
            print(f"Error - invalid parameter '{item_and_value[0]}'")
            continue

        try:
            if item_and_value[0] in inventory:
                raise DoublonError(f"Redundant item '{item_and_value[0]}' \
- discarding")
        except DoublonError as e:
            print(f"{e}")
            continue

        try:
            int(item_and_value[1])
        except ValueError as e:
            print(f"Quantity error for '{item_and_value[0]}' : {e}")
            continue

        inventory[item_and_value[0]] = item_and_value[1]

    print(inventory)
