#!/usr/bin/env python3
from engine import engine


def main():
    game = 'brain_prime'
    greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()