# import my gradient generator lib
from gradientor import gradient_generators as gd
import time
import os

# vars
stage = 0
name = "default"
choice = 1
# clear console function
def clear():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
# end game function
def endgame():
    gd.gradient_banner("Game Over", "#D4AF37", "#E0BFB8")
    print(f"you reached stage {stage}!")
    gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
    gd.gradient_text("Thanks for playing!", "#D4AF37", "#E0BFB8")
    gd.gradient_text("Created by: @butterific", "#D4AF37", "#E0BFB8")
def print_line():
    gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
# start of the game
gd.gradient_banner("Terminal Crawler", "#D4AF37", "#E0BFB8")
gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
gd.gradient_text("A fun, interactive terminal game which progresses through 25 pre generated stages!", "#D4AF37", "#E0BFB8")
# asks for the users name
name = input("To start, Please enter your name: ")
name = name[0:1].upper() + name[1:]
print(f"Hello, {name}! Welcome to Terminal Crawler!")
print("Let's begin!")
time.sleep(3)
clear()
gd.gradient_banner("Stage 1", "#D4AF37", "#E0BFB8")
gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
stage = 1
print(f"{name} finds a strange artifact on the wall...")
time.sleep(1.2)
print("As you approach it, you notice a strange symbol on the artifact...")
time.sleep(1.2)
print("The symbol is glowing, and you feel a strange energy emanating from it...")
choice = input("Do you want to touch the artifact? (y/n): ")
if choice.lower() == "y":
    print_line()
    print("You touch the artifact and feel a surge of energy!")
    time.sleep(1.2)
    print("The artifact begins to glow brighter and brighter...")
    time.sleep(1.2)
    print("Suddenly, you are transported to a new location!")
    time.sleep(1.2)
    clear()
    stage += 1
else:
    print_line()
    print("You decide not to touch the artifact and continue on your journey...")
    time.sleep(1.2)
    print("As you walk away, you feel a strange entity following you...")
    time.sleep(1.2)
    print("Suddenly, you are backstabbed and die on the spot...")
    time.sleep(1.2)
    clear()
    endgame()