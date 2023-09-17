import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question():
    start = random.randint(1, 99)
    step = random.randint(1, 11)
    length = random.randint(6, 11)
    hidden_position = random.randint(0, length - 1)
    progression = get_progression(start, step, length)
    right_answer = progression[hidden_position]
    progression[hidden_position] = '.. '
    question = " ".join(progression)
    return right_answer, question


def get_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(str(start + step * i))
    return progression
