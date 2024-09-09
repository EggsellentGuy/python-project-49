from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS
from brain_games.outsourced_functions import generation_calculate_question
import prompt



def calc_game():
    name = welcome_user()
    for i in range(MAX_RAUNDS):
        print(f"Question {generation_calculate_question}")
        

              

