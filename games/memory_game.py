import random
import time
from utils import clear_screen
import score

random_numbers = []
user_list = []

def generate_sequence(level):
    for i in range(level):
        random_numbers.append(random.randint(1, 101))  # You can adjust the range as needed
    print(random_numbers)
    time.sleep(0.7)  # Wait for 0.7 seconds
    clear_screen()

def get_list_from_user(level):
    for i in range(level):
        valid_input = False
        while not valid_input:
            user_input = input(f"Please enter {i + 1} number you remembered:  ")
            if user_input.isdigit():
                user_list.append(int(user_input))
                valid_input = True
            else:
                print("Invalid input. Please enter a numeric value.")

def is_list_equal(computer_numbers,user_numbers):
    if computer_numbers == user_numbers:
        return True
    else:
        return False

def play(level):
    generate_sequence(level)
    get_list_from_user(level)
    if is_list_equal(random_numbers,user_list):
        print("YOU WON!!!")
        score.add_score(level)
    else:
        print("YOU LOST!!!")




