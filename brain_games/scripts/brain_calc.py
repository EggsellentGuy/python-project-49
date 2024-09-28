#!/usr/bin/env python3
from brain_games.games import calc_game
from brain_games.main_game_func import main_game_function


def main():
    main_game_function(calc_game.Question_Generator_Calc, 
                       calc_game.CALC_RULES)


if __name__ == '__main__':
    main()
