#!/usr/bin/env python3
from brain_games.main_game_func import main_game_function
from brain_games.games.gcd_game import (
    GCD_QUESTION_CONST,
    Question_Generator_Gcd
)


def main():
    main_game_function(Question_Generator_Gcd, GCD_QUESTION_CONST)


if __name__ == '__main__':
    main()
