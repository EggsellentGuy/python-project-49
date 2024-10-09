import random


GAME_RULES = 'What number is missing in the progression?'


def generate_question():
    expression, correct_answer = generate_progression()
    return expression, correct_answer


def generate_progression():
    progression = []
    start = random.randint(1, 20)
    step = random.randint(1, 15)
    for _ in range(10):
        progression.append(start)
        start += step
    rand_index = random.randint(0, len(progression))
    hidden_element = progression[rand_index]
    progression[rand_index] = '..'
    progression_str = map(str, progression)
    progression_str = ' '.join(progression_str)
    expression = f"{progression_str}"
    return expression, hidden_element
