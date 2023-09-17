import prompt
# количество удачных попыток игры, по заданию - 3 штуки

ROUNDS_COUNT = 3


def start(game):
    print('Welcome to the Brain Games!\n'
          'May I have your name? ', end='')
    name = input()
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)

    for i in range(ROUNDS_COUNT):
        right_answer, question = game.get_question()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{right_answer}'."
                  f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
