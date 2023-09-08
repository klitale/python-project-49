import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    ran_first = random.randint(1, 1000)
    right_answer = ''
    if ran_first % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = ran_first
    return right_answer, question
