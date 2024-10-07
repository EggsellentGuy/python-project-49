#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.main_func import WELCOME_PHRASE


def main():
    print(WELCOME_PHRASE)
    welcome_user()


if __name__ == '__main__':
    main()
