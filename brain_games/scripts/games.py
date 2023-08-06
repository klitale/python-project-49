#!/usr/bin/env python3
import random, prompt


def brain_even():
    argument_first = random.randint(1, 1000)
    right_answer = ''
    if argument_first % 2 == 0:
        right_answer = 'yes'
    else: right_answer = 'no'
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {argument_first}')
    return right_answer


def brain_calc():
    argument_first = random.randint(1, 10)
    argument_second = random.randint(1, 10)
    operation = random.choice(['-', '+', '*'])
    right_answer = ''
    if operation == '-':
        right_answer = argument_first - argument_second
    elif operation == '+':
        right_answer = argument_first + argument_second
    else:
        right_answer = argument_first * argument_second
    print(f'Question: {argument_first} {operation} {argument_second}')
    return str(right_answer)
