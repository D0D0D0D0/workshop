import random

def le_number_guessing_game():
    chosen_number = random.randint(1, 100)

    while True:
        try:
            user_guess = int(input("Guess the number: "))
        except ValueError:
            print("Not a NUMBER! >:(")
            continue

        if user_guess < chosen_number:
            print("Too smol :c")
        elif user_guess > chosen_number:
            print("Too BIG!")
        else:
            print("You win! :D")
            break

le_number_guessing_game()