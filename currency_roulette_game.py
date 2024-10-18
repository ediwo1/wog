import requests
import score

def play(level):
    api_key = "fca_live_35VE25zmlE7RUmPxiRS9u5SOL63A7eKG58aRVELn"

    # API URL for fetching the latest exchange rates with USD as the base currency
    base_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency=USD"

    # Make the API request
    response = requests.get(base_url)

    # Parse the JSON response
    data = response.json()
    current_rate = 0
    if response.status_code == 200:
        for currency, rate in data['data'].items():
            if currency == 'ILS':
                # print(f"1 USD = {rate} {currency}")
                current_rate = rate
    else:
        print("Error fetching data:", data.get("message", "Unknown error"))

    if compare_results(level):
        print("YOU WON!!!")
        score.add_score(level)
    else:
        print("YOU LOST!!!")

    print(f"Exchange rates for 1 USD: {current_rate} ILS")

def get_money_interval(level):
    return 10 - level

def get_guess_from_user():
    valid_input = False
    while not valid_input:
        user_input = input(f"Try to guess. Choose number from 0 to 100: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 0 <= user_input <= 100:
                valid_input = True
                return user_input
            else:
                print('Your number is out of range. Please try again.')
        else:
            print("Invalid input. Please enter a numeric value.")

def compare_results(level):
    user_guess = get_guess_from_user()
    allowed_interval = get_money_interval(level)
    if user_guess in range(0,allowed_interval):
        return True
    else:
        return False


