#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    game = 'brain_even_logic'
    greeting = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()
