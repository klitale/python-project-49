#!/usr/bin/env python3
import random, prompt
from brain_games.scripts import games


def start(game, greeting):
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    print(greeting)
    i = 0
    right_answer = ''
    script = ''
    while i < 3:
        right_answer = eval(f'games.{game}()')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(right_answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
