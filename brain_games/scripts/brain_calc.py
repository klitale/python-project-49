#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    game = 'brain_calc_logic'
    greeting = 'What is the result of the expression?'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()
