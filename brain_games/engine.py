import prompt
# количество удачных попыток игры, по заданию - 3 штуки

ATTEMPTS = 3


def start(game):
    print('Welcome to the Brain Games!')
    print('May I have your name? ', end='')
    name = input()
    print(f'Hello, {name}!')
    # вытаскиваем приветстсиве из скрипта:
    print(game.DESCRIPTION)
    for attempt in range(ATTEMPTS):
        # вытаскиваем правильный ответ и вопрос из скрипта:
        right_answer, question = game.get_question()
        # вытаскиваем вопрос из скрипта:
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
