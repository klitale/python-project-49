import random


def main():
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
