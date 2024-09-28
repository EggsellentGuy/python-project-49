#!/usr/bin/env python3
from brain_games.main_game_func import main_game_function
from brain_games.games.even_game import (
    EVEN_RULES,
    Question_Generator_Even
)


def main():
    main_game_function(Question_Generator_Even, EVEN_RULES)


if __name__ == '__main__':
    main()
