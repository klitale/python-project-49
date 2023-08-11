import random


def main():
    argument_first = random.randint(2, 1223)
    i = 1
    right_answer = 'yes'
    while argument_first >= i:
        if argument_first % i == 0 and argument_first != i and i != 1:
            right_answer = 'no'
            break
        i += 1
    print(f'Question: {argument_first }')
    return str(right_answer)
