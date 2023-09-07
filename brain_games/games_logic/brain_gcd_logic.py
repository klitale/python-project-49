import random


def greeting():
    return 'Find the greatest common divisor of given numbers.'


def play():
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
    question = f'{argument_first} {argument_second}'
    return right_answer, question
