import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_question():
    start = random.randint(1, 99)
    step = random.randint(1, 11)
    hidden_position = random.randint(0, PROGRESSION_LENGTH - 1)
    progression = get_progression(start, step, PROGRESSION_LENGTH)
    right_answer = progression[hidden_position]
    progression[hidden_position] = '..'
    question = " ".join(progression)
    return right_answer, question


def get_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(str(start + step * i))
    return progression
