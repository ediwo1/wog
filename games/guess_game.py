import random
import score

def play(level):
    computer_choice = generate_number(level)
    user_choice = get_guess_from_user(level)
    print(f"Computer's choice: {computer_choice}")
    print(f"User's choice: {user_choice}")
    if compare_results(computer_choice,user_choice):
        print("YOU WON!!!")
        score.add_score(level)
    else:
        print("YOU LOST...")

def generate_number(level):
    computer_number = random.randint(0,level)
    return computer_number

def get_guess_from_user(level):
    valid_input = False
    while not valid_input:
        user_input = input(f"Try to guess. Choose number from 0 to {level}: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 0 <= user_input <= level:
                valid_input = True
                return user_input
            else:
                print('Your number is out of range. Please try again.')
        else:
            print("Invalid input. Please enter a numeric value.")

def compare_results(computer_number,user_input):
    if computer_number == user_input:
        return True
    else:
        return False
