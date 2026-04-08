#!usr/bin/env python3

import random


if __name__ == "__main__":
    print(" === Game Data Alchemist === \n")

    initial_list: list[str] = ["Jean", "jacques", "Pierre", "paul", "Michel",
                               "charles", "Bob", "alice"]
    print(f"Initial list of players : {initial_list}")

    second_list: list[str] = [name.capitalize() for name in initial_list]
    print(f"\nNew list with all names capitalized : {second_list}")

    third_list: list[str] = [name for name in initial_list
                             if name == name.capitalize()]
    print(f"\nNew list of capitalized names only : {third_list}")

    score_dict = {name: random.randint(0, 100) for name in second_list}
    print(f"\n\nScore dict : {score_dict}")

    average: float = sum(score_dict.values()) / len(score_dict)
    print(f"\nScore average : {round(average, 2)}")

    high_scores = {name: score for name, score in
                   score_dict.items() if score > average}
    print(f"\nHigh scores : {high_scores}")
