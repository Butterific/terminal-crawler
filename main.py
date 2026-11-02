# import my gradient generator lib
from gradientor import gradient_generators as gd
import time
import os
import sys

# vars
stage = 0
name = "default"
choice = 1
textdelayquick = 1.2
textdelay = 2.4
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
    sys.exit(0) 
def print_line():
    gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
# start of the game
gd.gradient_banner("Terminal Crawler", "#D4AF37", "#E0BFB8")
print_line()
gd.gradient_text("A fun, interactive terminal game which progresses through 10 stages!", "#D4AF37", "#E0BFB8")
# asks for the users name
name = input("To start, Please enter your name: ")
name = name[0:1].upper() + name[1:]
print(f"Hello, {name}! Welcome to Terminal Crawler!")
print("Let's begin!")
time.sleep(3)
clear()
# stage 1 code
gd.gradient_banner("Stage 1", "#D4AF37", "#E0BFB8")
print_line()
stage = 1
print(f"{name} finds a strange artifact on the wall...")
time.sleep(textdelayquick)
print("As you approach it, you notice a strange symbol on the artifact...")
time.sleep(textdelayquick)
print("The symbol is glowing, and you feel a strange energy emanating from it...")
choice = input("Do you want to touch the artifact? (y/n): ")
if choice.lower() == "y":
    print_line()
    print("You touch the artifact and feel a surge of energy!")
    time.sleep(textdelayquick)
    print("The artifact begins to glow brighter and brighter...")
    time.sleep(textdelayquick)
    print("Suddenly, you are transported to a new location!")
    time.sleep(textdelayquick)
    clear()
    stage += 1
else:
    print_line()
    print("You decide not to touch the artifact and continue on your journey...")
    time.sleep(textdelayquick)
    print("As you walk away, you feel a strange entity following you...")
    time.sleep(textdelayquick)
    print("Suddenly, you are backstabbed and die on the spot...")
    time.sleep(textdelayquick)
    clear()
    endgame()


# stage 2 code
gd.gradient_banner("Stage 2", "#D4AF37", "#E0BFB8")
print_line()
print(f"{name} finds themselves in a dark forest, with no memory of how they got there...")
time.sleep(textdelay)
print("As you look around, you notice a faint light in the distance...")
time.sleep(textdelay)
print("You decide to follow the light, hoping it will lead you to safety...")
time.sleep(textdelay)
print("As you get closer, you realize the light is coming from a small cabin...thats blue?")
time.sleep(textdelay)
print("You approach the cabin and notice a strange symbol on the door...")
time.sleep(textdelay)
print("That symbol looks familiar, you saw it on an artifact from your past...")
time.sleep(textdelay)
print("SUDDENLY, the door opens and a figure steps out...")
time.sleep(textdelay)
print("The figure is wearing a hooded cloak and you can't see their face...")
time.sleep(textdelay)
print("The figure speaks in a deep, menacing voice...")
time.sleep(textdelay)
gd.gradient_text(f"\'The trials of the Terminal Crawler await you...{name}\'", "#D4AF37", "#E0BFB8")
time.sleep(textdelay)
print("You have been chosen to face the trials of the Terminal Crawler!")
time.sleep(textdelay)
input("Press any key to continue...")
stage += 1

# stage 3 code
gd.gradient_banner("Stage 3", "#D4AF37", "#E0BFB8")
print_line()
print(f"{name} finds themselves in a vast, empty arena...")
time.sleep(textdelay)
print("As you look around, you notice a strange figure in the distance...")
time.sleep(textdelay)
print("The figure is wearing a hooded cloak and you can't see their face...")
time.sleep(textdelay)
print("The figure stares into your eyes and you feel a strange energy emanating from them...")
time.sleep(textdelay)
print("You feel a sudden urge to fight the figure, but you don't know why...")
time.sleep(textdelay)
print("The figure speaks in a deep, menacing voice...")
time.sleep(textdelay)
gd.gradient_text("COME FORTH!", "#8B0000", "#FF474C")