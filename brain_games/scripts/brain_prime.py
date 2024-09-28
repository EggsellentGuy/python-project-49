#!/usr/bin/env python3
from brain_games.main_game_func import main_game_function
from brain_games.games import prime_game


def main():
    main_game_function(prime_game.Question_Generator_Prime,
                       prime_game.PRIME_RULES)


if __name__ == '__main__':
    main()
