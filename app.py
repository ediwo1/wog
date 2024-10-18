import guess_game
import currency_roulette_game
import memory_game


def welcome():
    username = input("Please enter your username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey\n")

def start_play():
    games = [
         {
            "game_name": "Memory Game",
            "game_description": "a sequence of numbers will appear for 1 second and you have to guess it back.",
            "difficulty_level": 5
        },
        {
            "game_name": "Guess Game",
            "game_description": "guess a number and see if you chose like the computer.",
            "difficulty_level": 5
        },
        {
            "game_name": "Currency Roulette",
            "game_description": "try and guess the value of a random amount of USD in ILS",
            "difficulty_level": 5
        }
    ]

    total_number_of_games = len(games)
    for idx in range(total_number_of_games):
        print(f"{idx + 1}. {games[idx]['game_name']} - {games[idx]['game_description']}")

    game_to_play = 0
    level_to_play = 0
    max_difficulty_level = 0

    valid_input = False
    while not valid_input:
        user_input = input("Please enter game number you want to play:  ")
        if user_input.isdigit():
            game_to_play =  int(user_input)
            if 1 <= game_to_play <= total_number_of_games:
                print(f"You chose to play: {games[game_to_play - 1]['game_name']}")
                max_difficulty_level = games[game_to_play - 1]['difficulty_level']
                valid_input = True
            else:
                print("Please choose from the available options only")
        else:
            print("Invalid input. Please enter a numeric value.")

    valid_input = False
    while not valid_input:
        user_input = input(f"Please enter difficulty level to play from 1 to {max_difficulty_level}:  ")
        if user_input.isdigit():
            level_to_play = int(user_input)
            if 1 <= level_to_play <= max_difficulty_level:
                print(f"You chose difficulty level: {level_to_play}")
                valid_input = True
            else:
                print('You chose a wrong difficulty level')
        else:
            print("Invalid input. Please enter a numeric value.")

    if game_to_play == 1:
        print('Playing memory game')
        memory_game.play(level_to_play)
    elif game_to_play == 2:
        print('Playing guess game')
        guess_game.play(level_to_play)
    elif game_to_play == 3:
        print('Playing currency roulette')
        currency_roulette_game.play(level_to_play)
    else:
        print("Can't find the game")

