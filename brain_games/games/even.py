import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    random_number = random.randint(1, 1000)
    right_answer = ''
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = random_number
    return right_answer, question
