import prompt
from brain_games.constants import MAX_RAUNDS, WELCOME_PHRASE


def main_game_function(question_func, game_rules):
    print(WELCOME_PHRASE)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_rules)
    for _ in range(MAX_RAUNDS):
        correct_answer = question_func()
        user_answer = prompt.string('Your answer ')
        if str(correct_answer) == str(user_answer):
            print('Correct!')
            continue
        else:
            print(f"'{user_answer.lower()}' is wrong answer ;(. \
 Correct answer was '{correct_answer}'\nLet's try again, {name}!.")
            break
    else:
        print(f"Congratulations, {name}!")
