import random


def greeting():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    result = []
    argument_first = random.randint(1, 1000)
    right_answer = ''
    if argument_first % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = argument_first
    return right_answer, question

