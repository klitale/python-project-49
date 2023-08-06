#!/usr/bin/env python3
from engine import engine


def main():
    game = 'brain_progression'
    greeting = 'What number is missing in the progression?'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()