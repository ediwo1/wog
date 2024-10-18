import os
import utils

file_path = utils.scores_file_name

def add_score(level):
    points_of_winning = (level * 3) + 5
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            current_score = int(file.read())
        new_score = current_score + points_of_winning
    else:
        new_score = points_of_winning

    with open(file_path, 'w') as file:
        file.write(str(new_score))


