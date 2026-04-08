#!usr/bin/env python3

import typing_extensions
import random


def gen_event() -> typing_extensions.Generator:
    names: list[str] = ["Jean", "Jacques", "Pierre", "Paul", "Michel"]
    actions: list[str] = ["(1) move", "(2) run", "(3) grab", "(4) swim",
                          "(5) release"]

    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events_list: list[tuple]) -> typing_extensions.Generator:
    while len(events_list):
        event: tuple = random.choice(events_list)
        events_list.remove(event)
        yield event


if __name__ == "__main__":
    print(" === Game Data Stream Processor === \n")

    generator = gen_event()
    for i in range(10):
        (name, action) = next(generator)
        print(f"Event {i} : Player {name} did action {action}")

    ten_events: list[tuple] = []
    for i in range(10):
        ten_events.append(next(generator))
    print(f"\nBuilt list of ten events : {ten_events}")

    for event in consume_event(ten_events):
        print(f"\nGot event from list : {event}")
        print(f"Remains in the list : {ten_events}")
