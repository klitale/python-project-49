import random


def main():
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
