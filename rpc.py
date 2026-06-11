import random


def rpc_storage():
    rpc = {"rock" : "scissors",
           "paper" : "rock",
           "scissors" : "paper"}
    return rpc
    
    
def rpc_condition(rpc, bot_choice, user_choice):
    if bot_choice == user_choice:
        return "Draw"
    elif rpc[bot_choice] == user_choice:
        return(f"Bot Played {bot_choice.capitalize()} You Lost")
    else:
        return(f"Bot Played {bot_choice.capitalize()} You Won")


def rpc_game():
    rpc = rpc_storage()
    
    while True:
        user_rpc_score = 0
        bot_rpc_score = 0
        while True:
            user_choice = input("Enter Rock, Paper, Scissors [Type Quit To Stop] : ").lower().strip()
            if user_choice == "quit":
                break
            bot_choice = random.choice(["rock", "paper", "scissors"])
            result = rpc_condition(rpc, bot_choice, user_choice)
            if user_choice in rpc:
                if result == f"Bot Played {bot_choice.capitalize()} You Won":
                    user_rpc_score += 1
                    print(rpc_condition(rpc, bot_choice, user_choice))
                    print(user_rpc_score)
                    print(bot_rpc_score)
                elif result == f"Bot Played {bot_choice.capitalize()} You Lost":
                    bot_rpc_score += 1
                    print(rpc_condition(rpc, bot_choice, user_choice))
                    print(user_rpc_score)
                    print(bot_rpc_score)
            else:
                print("Choose Between Rock Paper Scissors")
            if user_rpc_score == 5:
                print("You Won The Round!")
                break
            elif bot_rpc_score == 5:
                print("Bot Won The Round!")
                break
        rpc_play_again = input("Do You Want To PLay? [y/n] : ").lower().strip()
        if rpc_play_again == "n":
            break
        elif rpc_play_again == "y":
            continue        
if __name__ == "__main__":
    rpc_game()