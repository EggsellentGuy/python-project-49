#!/usr/bin/env python3
from brain_games.main_game_func import main_game_function
from brain_games.games import gcd_game


def main():
    main_game_function(gcd_game.Question_Generator_Gcd, 
                       gcd_game.GCD_RULES)


if __name__ == '__main__':
    main()
