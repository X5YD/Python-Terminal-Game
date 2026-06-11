import random


def geuss_conditions(user_guess, bot_guess):
    if user_guess < bot_guess:
        return "Too Low"
    elif user_guess > bot_guess:
        return "Too High"
    else:
        return "Correct"

def numb_geuss():
    bot_guess = random.randint(1, 100)
    guess = 0
    while True:
        try:
            user_input = input("The Game Has Decided A Number, Your Guess? [Type Quit To Stop] : ")
            if user_input.lower().strip() == "quit":
                break
            user_guess = int(user_input)
            guess_result = geuss_conditions(user_guess, bot_guess)
            if not guess_result == "Correct":
                guess += 1
                print(guess_result)
                print(f"Guess Count : {guess}")
            else:
                guess += 1
                print(guess_result)
                print(f"You Have Completed The Game In {guess} Guesses! ")
                break
            
        except ValueError:
            print("Thats Not A Number...! ")
if __name__ == "__main__":
    numb_geuss()