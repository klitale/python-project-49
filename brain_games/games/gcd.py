import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question():
    right_answer, ran_first, ran_second = calc_gcd()
    question = f'{ran_first} {ran_second}'
    return right_answer, question


def calc_gcd():
    ran_first = random.randint(1, 100)
    ran_second = random.randint(1, 100)
    if ran_first == ran_second:
        minimum: int = ran_first
    else:
        maximum: int = max(ran_first, ran_second)
        minimum: int = min(ran_first, ran_second)
        while 0 < (maximum % minimum):
            rem_of_div = maximum % minimum
            maximum = minimum
            minimum = rem_of_div
    return minimum, ran_first, ran_second
