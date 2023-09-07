#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games_logic import brain_prime_logic


def main():
    start_game(brain_prime_logic)


if __name__ == '__main__':
    main()
