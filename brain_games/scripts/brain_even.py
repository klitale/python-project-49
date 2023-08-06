#!/usr/bin/env python3
from engine import engine


def main():
    game = 'brain_even'
    greeting = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()
