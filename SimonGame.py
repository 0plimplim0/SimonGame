import random
import os
import time
from colorama import Fore, Style

print("Welcome to Simon Game!")

def clear_console():
    os.system("clear")

def red():
    clear_console()
    print("   _      _      _\n  /" + Fore.RED + "0" + Style.RESET_ALL + "\\    / \\    / \\ \n |" + Fore.RED + "000" + Style.RESET_ALL + "|  |___|  |___|")
    time.sleep(0.7)

def yellow():
    clear_console()
    print("   _      _      _\n  / \\    /" + Fore.YELLOW + "0" + Style.RESET_ALL + "\\    / \\ \n |___|  |" + Fore.YELLOW + "000" + Style.RESET_ALL + "|  |___|")
    time.sleep(0.7)

def green():
    clear_console()
    print("   _      _      _\n  / \\    / \\    /" + Fore.GREEN + "0" + Style.RESET_ALL + "\\ \n |___|  |___|  |" + Fore.GREEN + "000" + Style.RESET_ALL + "|")
    time.sleep(0.7)

def help():
    print("""------------
Commands available
------------
play : Starts the game.
exit : Exit the game.
help : Shows available commands.
score : Shows highest score.
------------""")

def high_score():
    print(f"The highest score was {highScore}")


colors = ["red", "yellow", "green"]
highScore = 0


while True: 
    usrInput = input("Type 'play', 'help' or 'exit': ").lower()
    if usrInput == "play":
        score = 0
        print("Game starts in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        os.system("clear")
        while True:
            answer = []
            for i in range(score + 1):
                color = random.choice(colors)
                if color == "red":
                    red()
                    answer.append("red")
                elif color == "yellow":
                    yellow()
                    answer.append("yellow")
                elif color == "green":
                    green()
                    answer.append("green")
                
            usrAnswer = input("Your answer: ").lower().split()
            if usrAnswer == answer:
                print("Correct!")
                score += 1
                if score > highScore:
                    highScore = score
                    print(f"New high score: {highScore}")
                time.sleep(1)
            else:
                print(f"Game Over! \nYour score was {score}")
                break

    elif usrInput == "exit":
        print("Goodbye.")
        break
    elif usrInput == "help":
        help()
    elif usrInput == "score":
        high_score()
    else: print("Invalid command.")