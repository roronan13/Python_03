#!usr/bin/env python3

import sys

if __name__ == "__main__":
    print(" === Command Quest === \n")
    print(f"Program name : {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided !")
    else:
        print(f"Arguments received : {len(sys.argv) - 1}")

    i: int = 1
    for i in range(i, len(sys.argv)):
        print(f"Argument {i} : {sys.argv[i]}")

    print(f"Total arguments : {len(sys.argv)}")
