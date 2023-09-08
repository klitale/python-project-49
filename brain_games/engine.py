import prompt
# количество удачных попыток игры, по заданию - 3 штуки

ATTEMPTS = 3

def start_game(script):
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    # вытаскиваем приветстсиве из скрипта:
    print(script.greeting())
    for attempt in range(ATTEMPTS):
        # вытаскиваем правильный ответ и вопрос из скрипта:
        right_answer, question = script.play()
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
