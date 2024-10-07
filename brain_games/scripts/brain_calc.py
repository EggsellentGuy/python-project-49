#!/usr/bin/env python3
from brain_games.games import calc_game
from brain_games.main_game_func import play_games


def main():
    play_games(calc_game)


if __name__ == '__main__':
    main()
