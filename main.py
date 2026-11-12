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

# for debug/ delete later
textdelay = float(input("Please enter your preferred text delay (in seconds): "))
textdelayquick = float(input("Please enter your preferred quick text delay (in seconds): "))
# end of debug 


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
clear()
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
time.sleep(textdelay)
input("Press any key to continue...")
clear()
stage += 1

# stage 4 code
gd.gradient_banner("Stage 4", "#D78F7D", "#E82C06")
print_line()
from bossfight1 import startbossfight1

print("LET THE BATTLE BEGIN!")
time.sleep(textdelayquick)
print("WASD to move, and R to attack!")
time.sleep(3)
result = startbossfight1(
    "bossfight1",
    win_var="bossDefeated",
    lose_var="playerDead",
    watch_vars=["playerHP", "bossHP", "turns"],
)
if result["won"]:
    print(f"You won! HP left: {result['vars']['playerHP']}")
    print(f"Turns taken: {result['vars']['turns']}")
    gd.gradient_text("You have defeated the boss and can now proceed to the next stage!", "#D78F7D", "#E82C06")
    input=("Press any key to continue...")
    input=("Press any key to continue... x2")
    stage += 1
else:
    endgame()

gd.gradient_banner("Stage 5", "#FF0000", "#80EF80")
print_line()
print("You sudently plop back to the same room where you found the artifact, but this time, the artifact is gone...")
time.sleep(textdelay)
print("The room has an ominuus, eerie feeling to it, and you feel a sense of dread wash over you...")
time.sleep(textdelay)
gd.gradient_text("SUDDENLY, the floor begins to shake...", "#FF0000", "#80EF80")
time.sleep(textdelay)
print("You hear a loud rumbling noise, and the walls begin to crumble...")
time.sleep(textdelay)
print("You are forced to make a desicion as the room collapses around you...")
time.sleep(textdelay)
choice = input("Do you choose to grab the wall and hold on for your life...or fall down into the depts hoping for a way out? (grab/fall): ")
if choice.lower() == "fall":
    print_line()
    print("You choose to fall down into the depts, at the speed of light, a deep voice echoes through the room...")
    time.sleep(textdelayquick)
    print("\"Surrender now or prepare for a fight\"")
    time.sleep(textdelayquick)
    print("You fall for hours, but eventually you land next to a...? clone of yourself???")
    time.sleep(textdelay)
    print("HOLD THAT WASNT PART OF THE SCRIPT")
    time.sleep(textdelay)
    gd.gradient_text("Ì̴̧͔ ̴̜̱͓̾̂͝W̵̤͒͋Ì̸̛̭͉L̵̡͖̱͌͂L̸̢̢͘͝ ̵̛̮̝͐͗B̷̨̺̰̌̍͐Ȩ̵̻̮̀̍̐ ̶̧̼̐͋Ţ̸̐͋A̵̱̺͍͐K̶̪͛͝ͅI̷͔͔͠N̴̗̿Ḡ̷̜͇̗ ̷̙́̔͘ͅC̶̟̭̝͋O̵̝͂͠N̶̙̻̘̍T̴̡̳̄Ŗ̶̭̩͑͑Ǫ̸͚̖̆̊̐L̴̖͎̿ ̴͙̣̦̈́̋͆O̴̼̠̱̽F̸̢̫̳̾̈́ ̵̧̹͇̍T̴̢̢͙̈̇H̸̘̦̐̂̕I̴̛̤̼͇͒S̴̳̀͗̕ ̴̧̻͋N̴͎̆̿O̶̞͛͂̐W̸̦̳͈̌", "#FF0000", "#8b0000")
    clear()
    stage += 1
else:
    print_line()
    print("You hand on for hours, but the walls are crumbling and you are forced to let go...")
    time.sleep(textdelay)
    print("You took too long, the floor incommpases with spikes, as sharp as a sword, and you fall into the depts...")
    time.sleep(textdelay)
    print("You die on impact never seen again...")
    time.sleep(textdelay + 2)
    clear()
    endgame()