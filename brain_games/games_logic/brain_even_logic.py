import random


def main():
    argument_first = random.randint(1, 1000)
    right_answer = ''
    if argument_first % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {argument_first}')
    return right_answer
