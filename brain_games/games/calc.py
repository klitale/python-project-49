import random


DESCRIPTION = 'What is the result of the expression?'


def get_question():
    ran_first = random.randint(1, 10)
    ran_second = random.randint(1, 10)
    operation = random.choice(['-', '+', '*'])
    right_answer = ''
    if operation == '-':
        right_answer = ran_first - ran_second
    elif operation == '+':
        right_answer = ran_first + ran_second
    elif operation == '*':
        right_answer = ran_first * ran_second
    question = f'{ran_first} {operation} {ran_second}'
    return right_answer, question
