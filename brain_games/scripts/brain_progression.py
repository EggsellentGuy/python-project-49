#!/usr/bin/env python3
from brain_games.constants import WELCOME_PHRASE
from brain_games.games.progression_game import progression_game


def main():
    print(WELCOME_PHRASE)
    progression_game()


if __name__ == '__main__':
    main()
