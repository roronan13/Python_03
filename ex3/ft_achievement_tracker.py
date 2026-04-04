#!usr/bin/env python3

import random


class Player:
    def __init__(self, name: str, achievements: set[str]):
        self.name = name
        self.achievements = achievements


def gen_player_achievements() -> set[str]:
    all_achievements: list = ["(1) Crafting genius", "(2) Strategist",
                              "(3) World savior", "(4) Speed runner",
                              "(5) Survivor", "(6) Master explorer",
                              "(7) Treasure hunter", "(8) Unstoppable"]
    result: set[str] = set()
    randon_nbr: int = random.randint(1, len(all_achievements))

    for i in range(randon_nbr):
        result.add(random.choice(all_achievements))

    return result


if __name__ == "__main__":
    print(" === Achievement tracker system === \n")
    set_1: set[str] = gen_player_achievements()
    player_1 = Player("Player_1", set_1)
    set_2: set[str] = gen_player_achievements()
    player_2 = Player("Player_2", set_2)
    set_3: set[str] = gen_player_achievements()
    player_3 = Player("Player_3", set_3)
    set_4: set[str] = gen_player_achievements()
    player_4 = Player("Player_4", set_4)

    print(f"{player_1.name} : {player_1.achievements}")
    print(f"{player_2.name} : {player_2.achievements}")
    print(f"{player_3.name} : {player_3.achievements}")
    print(f"{player_4.name} : {player_4.achievements}")
    
    print(f"\nAll distinct achievements : {set.union(player_1.achievements,
                                                     player_2.achievements,
                                                     player_3.achievements,
                                                     player_4.achievements)}")
    
    print(f"\nCommon achievements : {set.intersection(player_1.achievements,
                                                      player_2.achievements,
                                                      player_3.achievements,
                                                      player_4.achievements)}")
    