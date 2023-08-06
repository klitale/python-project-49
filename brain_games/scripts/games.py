#!/usr/bin/env python3
import random, prompt
from typing import Any


def brain_even():
    argument_first = random.randint(1, 1000)
    right_answer = ''
    if argument_first % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
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


def brain_gcd():
    minimum = 0
    maximum = 0
    rem_of_div = 0
    argument_first = random.randint(1, 100)
    argument_second = random.randint(1, 100)
    if argument_first == argument_second:
        right_answer = argument_first
    else:
        maximum: int = max(argument_first, argument_second)
        minimum: int = min(argument_first, argument_second)
        while 0 < (maximum % minimum):
            rem_of_div = maximum % minimum
            maximum = minimum
            minimum = rem_of_div
    right_answer = minimum
    print(f'Question: {argument_first} {argument_second}')
    return str(right_answer)


def brain_progression():
    argument_first = random.randint(1, 99)
    step = random.randint(1, 11)
    length = random.randint(4, 10)
    next_argument = argument_first
    progression = []
    while 0 < length:
        next_argument = next_argument + step
        progression.append(next_argument)
        length -= 1
    random_element = random.randint(0, len(progression))
    random_element = progression[random_element]
    right_answer = random_element
    question = ''
    for element in progression:
        if int(random_element) == int(element):
            question += '.. '
        else:
            question += f'{str(element)} '
    print(f'Question: {question}')
    return str(right_answer)
