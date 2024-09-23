import random


PROGRESSION_QUESTION_CONST = 'What number is missing in the progression?'


def Question_Generator_Progression():
    correct_answer = generate_progression()
    return correct_answer


def generate_progression():
    progression = []
    start = random.randint(1, 20)
    step = random.randint(1, 15)
    for _ in range(10):
        progression.append(start)
        start += step
    rand_index = random.randint(0, len(progression) - 1)
    hidden_element = progression.pop(rand_index)
    progression.insert(rand_index, '..')
    progression_str = map(str, progression)
    progression_str = ' '.join(progression_str)
    print(f"Question: {progression_str}")
    return hidden_element
