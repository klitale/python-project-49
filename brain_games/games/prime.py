import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    ran = random.randint(2, 1223)
    question = ran
    right_answer = is_prime(ran)
    return right_answer, question


def is_prime(ran):
    i = 1
    right_answer = 'yes'
    while ran >= i:
        if ran % i == 0 and ran != i and i != 1:
            right_answer = 'no'
            break
        i += 1
    return right_answer
