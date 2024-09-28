#!/usr/bin/env python3
from brain_games.main_game_func import main_game_function
from brain_games.games.progression_game import (
    PROGRESSION_RULES,
    Question_Generator_Progression
)


def main():
    main_game_function(Question_Generator_Progression, 
                       PROGRESSION_RULES)


if __name__ == '__main__':
    main()
