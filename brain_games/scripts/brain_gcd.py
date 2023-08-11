#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    game = 'brain_gcd_logic'
    greeting = 'Find the greatest common divisor of given numbers.'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()
