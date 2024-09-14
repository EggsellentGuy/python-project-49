#!/usr/bin/env python3
from brain_games.constants import WELCOME_PHRASE
from brain_games.games.prime_game import prime_game


def main():
    print(WELCOME_PHRASE)
    prime_game()


if __name__ == '__main__':
    main()
