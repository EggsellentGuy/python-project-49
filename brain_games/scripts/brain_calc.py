#!/usr/bin/env python3
from brain_games.games.calc_game import (
    CALC_RULES,
    Question_Generator_Calc
)
from brain_games.main_game_func import main_game_function


def main():
    main_game_function(Question_Generator_Calc, CALC_RULES)


if __name__ == '__main__':
    main()
