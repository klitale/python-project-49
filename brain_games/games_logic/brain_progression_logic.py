import random


def greeting():
    return 'What number is missing in the progression?'


def play():
    argument_first = random.randint(1, 99)
    step = random.randint(1, 11)
    length = random.randint(6, 11)
    next_argument = argument_first
    progression = []
    while 0 < length:
        next_argument = next_argument + step
        progression.append(next_argument)
        length -= 1
    random_element = random.randint(0, len(progression) - 1)
    random_element = progression[random_element]
    right_answer = random_element
    question = ''
    for element in progression:
        if int(random_element) == int(element):
            question += '.. '
        else:
            question += f'{str(element)} '
    return right_answer, question
