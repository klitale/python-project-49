import prompt
# количество удачных попыток игры, по заданию - 3 штуки

ATTEMPTS = 3


def greeting():
    print('Welcome to the Brain Games!\n'
          'May I have your name? ', end='')
    name = input()
    print(f'Hello, {name}!')
    return name


def start(game):
    name = greeting()
    print(game.DESCRIPTION)
    for attempt in range(ATTEMPTS):
        right_answer, question = game.get_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(right_answer):
            print('Correct!')
            right_answer = ''
            question = ''
            if attempt == 2:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{right_answer}'."
                  f"\nLet's try again, {name}!")
            break
