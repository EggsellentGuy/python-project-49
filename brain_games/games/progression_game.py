from brain_games.cli import welcome_user
from brain_games.outsourced_functions import is_user_win
from brain_games.constants import MAX_RAUNDS
import prompt
import random


def progression_game():
    name = welcome_user()
    print('What number is missing in the progression?')
    for _ in range(MAX_RAUNDS):
        correct_answer = generate_progression()
        user_answer = prompt.string('Your answer ')
        if is_user_win(user_answer, correct_answer, name):
            continue
        else:
            break
    else:
        print(f'Congratulations, {name}!')


def generate_progression():
    progression = []
    start = random.randint(1, 20)
    step = random.randint(1, 15)
    for i in range(10):
        progression.append(start)
        start += step
    rand_index = random.randint(0, len(progression) - 1)
    hidden_element = progression.pop(rand_index)
    progression.insert(rand_index, '..')
    progression_str = map(str, progression)
    progression_str = ' '.join(progression_str)
    print(f"Question: {progression_str}")
    return hidden_element
