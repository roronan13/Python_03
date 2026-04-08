#!usr/bin/env python3

import sys


class DoublonError(Exception):
    def __init__(self, error_message: str):
        super().__init__(error_message)


def get_percentage(value: int, total: int) -> float:
    if total == 0:
        return 0

    percentage: float = (value * 100) / total
    return round(percentage, 1)


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

        inventory[item_and_value[0]] = int(item_and_value[1])

    print(f"Got inventory : {inventory}")
    print(f"Item list : {list(inventory.keys())}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the items : {total}")

    for key, value in inventory.items():
        print(f"Item {key} represents {get_percentage(value, total)}%")

    most_key: str = max(inventory, key=inventory.get)
    most_value: int = inventory[most_key]
    print(f"\nItem most abundant : {most_key} with quantity {most_value}")
    min_key: str = min(inventory, key=inventory.get)
    min_value: int = inventory[min_key]
    print(f"Item least abundant : {min_key} with quantity {min_value}")

    inventory.update({"one_last_item": 10})
    print(f"Updated inventory : {inventory}")
