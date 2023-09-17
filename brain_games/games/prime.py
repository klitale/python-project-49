import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    random_number = random.randint(3, 1223)
    question = random_number
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return right_answer, question


def is_prime(number):
    i = 1
    while i <= number:
        if number % i == 0 and number != i and i != 1:
            return False
        i += 1
    return True
