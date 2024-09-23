#!/usr/bin/env python3
from brain_games.main_game_func import main_game_function
from brain_games.games.prime_game import (
    PRIME_QUESTION_CONST,
    Question_Generator_Prime
)


def main():
    main_game_function(Question_Generator_Prime, PRIME_QUESTION_CONST)


if __name__ == '__main__':
    main()
