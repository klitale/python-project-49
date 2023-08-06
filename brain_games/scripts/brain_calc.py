#!/usr/bin/env python3
from engine import engine


def main():
    game = 'brain_calc'
    greeting = 'What is the result of the expression?'
    engine.start(game, greeting)


if __name__ == '__main__':
    main()
