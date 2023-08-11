#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    game = 'brain_prime_logic'
    greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()
