import random
import time

def dice_ascii():
    dice_art = {
        1: ("┌─────────┐",
            "|         |",
            "|    ●    |",
            "|         |",
            "└─────────┘"),
        2: ("┌─────────┐",
            "| ●       |",
            "|         |",
            "|       ● |",
            "└─────────┘"),
        3: ("┌─────────┐",
            "| ●       |",
            "|    ●    |",
            "|       ● |",
            "└─────────┘"),
        4: ("┌─────────┐",
            "| ●     ● |",
            "|         |",
            "| ●     ● |",
            "└─────────┘"),
        5: ("┌─────────┐",
            "| ●     ● |",
            "|    ●    |",
            "| ●     ● |",
            "└─────────┘"),
        6: ("┌─────────┐",
            "| ●     ● |",
            "| ●     ● |",
            "| ●     ● |",
            "└─────────┘"),
    }
    return dice_art

def dice_condition(bot_dice, user_dice):
        if user_dice < bot_dice:
            return "You Lost...!"
        elif user_dice > bot_dice:
            return "You Won...!"
        else:
            return ("draw")
        


def dice_game():
    dice_art = dice_ascii()
    score = 0
    bot_score = 0
    while True:
            score = 0
            bot_score = 0
            while True:
                bot_dice = random.randint(1, 6)
                user_dice = random.randint(1, 6)
                time.sleep(1)
                print(f"Bot Dice : {bot_dice}")
                for bot_value in dice_art.get(bot_dice):
                    print(bot_value)
                time.sleep(1)
                print(f"Your Dice : {user_dice}")

                for user_value in dice_art.get(user_dice):
                    print(user_value)

                result = dice_condition(bot_dice, user_dice)
                if result == "You Won...!":
                    score += 1
                elif result == "You Lost...!":
                    bot_score += 1
                print(result)
                if score == 5:
                    print("You Won The Match")
                    break
                elif bot_score == 5:
                    print("Bot Won The Match")
                    break
            time.sleep(1)
            play_again = input("Do You Want To Play Again? [y/n] : ")
            if play_again.lower().strip() == "y":
                    continue
            else:
                break
if __name__ == "__main__":
    dice_game()