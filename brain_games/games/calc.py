import random


DESCRIPTION = 'What is the result of the expression?'


def get_question():
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    operation = random.choice(['-', '+', '*'])
    right_answer = ''
    if operation == '-':
        right_answer = random_number1 - random_number2
    elif operation == '+':
        right_answer = random_number1 + random_number2
    elif operation == '*':
        right_answer = random_number1 * random_number2
    question = f'{random_number1} {operation} {random_number2}'
    return right_answer, question
