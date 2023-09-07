import random


def greeting():
    return 'What is the result of the expression?'


def play():
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
    question = f'{argument_first} {operation} {argument_second}'
    return right_answer, question
