#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.even_game import even_game


def main():
    welcome_user()
    even_game()


if __name__ == '__main__':
    main()