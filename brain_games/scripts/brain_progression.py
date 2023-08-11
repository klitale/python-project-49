#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    game = 'brain_progression_logic'
    greeting = 'What number is missing in the progression?'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()
