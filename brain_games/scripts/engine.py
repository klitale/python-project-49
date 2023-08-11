import prompt

from brain_games.games_logic import (brain_gcd_logic, brain_progression_logic, brain_prime_logic, brain_even_logic,
                                     brain_calc_logic) # noqa: 401


def start(game, greeting):
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    print(greeting)
    for question in range(3):
        right_answer = eval(f'{game}.main()')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(right_answer):
            print('Correct!')
            if question == 2:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{right_answer}'."
                  f"\nLet's try again, {name}!")
            break
