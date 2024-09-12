#!/usr/bin/env python3
from brain_games.games.gcd_game import gcd_game
from brain_games.constants import WELCOME_PHRASE


def main():
    print(WELCOME_PHRASE)
    gcd_game()


if __name__ == '__main__':
    main()
