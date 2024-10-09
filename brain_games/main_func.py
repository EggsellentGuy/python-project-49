import prompt


MAX_RAUNDS = 3
WELCOME_PHRASE = 'Welcome to the Brain Games!'


def run(game):
    print(WELCOME_PHRASE)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.GAME_RULES)
    for _ in range(MAX_RAUNDS):
        question, correct_answer = game.generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer ')
        if str(correct_answer) == str(user_answer):
            print('Correct!')
        else:
            print(f"'{user_answer.lower()}' is wrong answer ;(. \
 Correct answer was '{correct_answer}'\nLet's try again, {name}!.")
            break
    else:
        print(f"Congratulations, {name}!")
