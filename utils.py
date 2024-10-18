import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

scores_file_name = "Scores.txt"
bad_return_code = 0
