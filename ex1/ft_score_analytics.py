#!usr/bin/env python3

import sys


def is_numeric(score: str) -> int:
    return int(score)


if __name__ == "__main__":
    print(" === Player Score Analytics === \n")

    if len(sys.argv) == 1:
        print("No scores provided. Usage : python3 \
ft_score_analytics.py <score_1> <score_2> ...")
        sys.exit()

    scores_list: list = []
    i: int = 1
    for i in range(i, len(sys.argv)):
        try:
            score_int: int = is_numeric(sys.argv[i])
            scores_list.append(score_int)
        except ValueError:
            print(f"Invalid parameter : '{sys.argv[i]}'")

    if len(scores_list) == 0:
        print("No scores provided. Usage : python3 \
ft_score_analytics.py <score_1> <score_2> ...")
        sys.exit()

    print(f"Scores processed : {scores_list}")

    print(f"Total players : {len(scores_list)}")

    print(f"Total score : {sum(scores_list)}")

    print(f"Average score : {sum(scores_list) / len(scores_list)}")

    print(f"High score : {max(scores_list)}")

    print(f"Low score : {min(scores_list)}")

    print(f"Score range : {max(scores_list) - min(scores_list)}")
