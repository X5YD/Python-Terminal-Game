from number_guess import numb_geuss
from rpc import rpc_game
from dice import dice_game

def game_terminal():
    try:
        print("Rock Paper Scissors : 1 \nGuessing The Number : 2 \nDice : 3")
        game_choice = int(input("Which Game Do You Want To Play? : "))
        if game_choice == 1:
            rpc_game()
        elif game_choice == 2:
            numb_geuss()
        elif game_choice == 3:
            dice_game()
        else:
            print(f"Game {game_choice} Has Not Been Added Yet :")
    except ValueError:
        print("Enter A Number..!")
    
game_terminal()