# import my gradient generator lib
from gradientor import gradient_generators as gd
import time
import os
import sys
import random

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
    print(f"You reached stage {stage}!")
    gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
    gd.gradient_text("Thanks for playing!", "#D4AF37", "#E0BFB8")
    gd.gradient_text("Created by: @butterific", "#D4AF37", "#E0BFB8")
    sys.exit(0) 
def print_line():
    gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
# start of the game
gd.gradient_banner("Terminal Crawler", "#D4AF37", "#E0BFB8")
print_line()
gd.gradient_text("A fun, interactive terminal game that progresses through 10 stages!", "#D4AF37", "#E0BFB8")
# asks for the users name
name = input("To start, please enter your name: ")
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
print("As you get closer, you realize the light is coming from a small cabin... that's blue?")
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
gd.gradient_text(f"'The trials of the Terminal Crawler await you... {name}'", "#D4AF37", "#E0BFB8")
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
    input("Press any key to continue...")
    input("Press any key to continue... x2")
    stage += 1
else:
    endgame()
clear()
# code for stage 5
gd.gradient_banner("Stage 5", "#FF0000", "#80EF80")
print_line()
print("You suddenly plop back into the same room where you found the artifact, but this time, the artifact is gone...")
time.sleep(textdelay)
print("The room has an ominous, eerie feeling to it, and you feel a sense of dread wash over you...")
time.sleep(textdelay)
gd.gradient_text("SUDDENLY, the floor begins to shake...", "#FF0000", "#80EF80")
time.sleep(textdelay)
print("You hear a loud rumbling noise, and the walls begin to crumble...")
time.sleep(textdelay)
print("You are forced to make a decision as the room collapses around you...")
time.sleep(textdelay)
choice = input("Do you grab the wall and hold on for your life, or fall into the depths hoping for a way out? (grab/fall): ")
if choice.lower() == "fall":
    print_line()
    print("You choose to fall into the depths. At the speed of light, a deep voice echoes through the room...")
    time.sleep(textdelayquick)
    print("\"Surrender now or prepare for a fight\"")
    time.sleep(textdelayquick)
    print("You fall for hours, but eventually you land next to a...? clone of yourself???")
    time.sleep(textdelay)
    print("WAIT, THAT WASN'T PART OF THE SCRIPT")
    time.sleep(textdelay)
    gd.gradient_text("I̷̴ W̴̸I̸̵L̴̷L̵̸ B̸̴E̷̵ T̴̸A̷̵K̴̷I̸̵N̴̷G̵̸ C̷̴O̵̸N̴̷T̸̵R̴̷O̵̸L̷̴ O̵̸F̴̷ T̸̵H̴̷I̵̸S̷̴ N̵̸O̴̷W̸̵", "#FF0000", "#8b0000")
    input("Press any key to continue...")
    clear()
    stage += 1
else:
    print_line()
    print("You hold on for hours, but the walls are crumbling and you are forced to let go...")
    time.sleep(textdelay)
    print("You took too long. The floor opens into spikes as sharp as swords, and you fall into the depths...")
    time.sleep(textdelay)
    print("You die on impact, never to be seen again...")
    input("Press any key to continue...")
    time.sleep(textdelay + 2)
    clear()
    endgame()
clear()
# code for stage 6
gd.gradient_banner("Stage 6", "#FF0000", "#80EF80")
print_line()
print(f"{name}, I have brought you here, your previous guide has been taken from you, and now you must face the trials of the Terminal Crawler alone...")
time.sleep(textdelay)
print("\x1B[3m You notice skulls on the walls as the spikes rise around you, showing one possible outcome of your previous choice. You feel a sense of dread wash over you... \x1B[0m")
time.sleep(textdelay)
print("You notice a strange figure in the distance, it is wearing a hooded cloak and you can't see their face...")
time.sleep(textdelay)
print("The figure stares into your eyes and you feel a strange energy emanating from them...")
time.sleep(textdelay)
print("You feel a sudden urge to fight the figure, but you don't know why...")
time.sleep(textdelay)
print("The figure speaks in a deep, menacing voice...")
time.sleep(textdelay)
gd.gradient_text("W̷̴H̴̸O̸̵ A̴̷R̵̸E̸̴ Y̷̵O̴̸U̷̵", "#8B0000", "#FF474C")
time.sleep(textdelay)
input("Press any key to continue...")
clear()

# code for stage 7
gd.gradient_banner("Stage 7", "#FF0000", "#80EF80")
print_line()
stage = 7
print(f"The figure tilts its head. For the first time, it sounds afraid, {name}...")
time.sleep(textdelay)
print("You reach for the artifact, but your hand passes through empty air...")
time.sleep(textdelay)
print("The figure slowly removes its hood, revealing your own face beneath it.")
time.sleep(textdelay)
gd.gradient_text(f'"You keep asking who I am. The better question is: who told you that you are {name}?"', "#FF0000", "#8B0000")
time.sleep(textdelay)
print("Every light in the room flickers. Somewhere beyond the walls, a keyboard begins to type.")
time.sleep(textdelay)
print("A message appears on the floor, written in the same glowing symbols as the artifact:")
time.sleep(textdelay)
gd.gradient_text("THE CRAWLER IS NOT THE ONE BEING TESTED.", "#FF0000", "#8B0000")
time.sleep(textdelay)
print("The figure points behind you. The doorway is open, but the darkness beyond it is breathing.")
time.sleep(textdelay)
choice = input("Do you trust the figure, or enter the doorway? (trust/enter): ")
if choice.lower() == "trust":
    print_line()
    print("You turn back toward the figure...")
    time.sleep(textdelayquick)
    print("It smiles with your mouth and reaches for the controls.")
    time.sleep(textdelayquick)
    gd.gradient_text('"Finally. Now I can play as you."', "#FF0000", "#8B0000")
    input("Press any key to continue...")
    endgame()

else:
    print_line()
    print("You step through the doorway. The darkness closes behind you, but the terminal keeps running.")
    time.sleep(textdelayquick)
    print("From the other side, your own voice whispers: 'Good choice.'")
    time.sleep(textdelayquick)
input("Press any key to continue...")
clear()


# code for stage 8
gd.gradient_banner("Stage 8", "#FF0000", "#80EF80")
print_line()
stage = 8
print("You find yourself in a room filled with monitors, each displaying a different scene from your past.")
time.sleep(textdelay)
print("You see yourself as a child, playing with friends, and then as a teenager, making mistakes and learning from them.")
time.sleep(textdelay)
print("You see yourself as an adult, facing challenges and overcoming obstacles.")
time.sleep(textdelay)
print("The scenes are all connected, showing the journey of your life from start to finish.")
time.sleep(textdelay)
input("Press any key to continue...")
clear()

# code for stage 9
gd.gradient_banner("Stage 9", "#FF0000", "#80EF80")
print_line()
stage = 9
print("You are now in the final stage of the game.")
time.sleep(textdelay)
print("You see a door in front of you, but it is locked.")
time.sleep(textdelay)
input("Press any key to continue...")
clear()

# code for stage 10
gd.gradient_banner("Stage 10", "#FF0000", "#80EF80")
print_line()
stage = 10
print("The locked door dissolves the moment you stop trying to open it...")
time.sleep(textdelay)
print("Beyond it sits the thing that has been watching you through every monitor.")
time.sleep(textdelay)
gd.gradient_text("THE NULL CRAWLER", "#FF0000", "#8B0000")
time.sleep(textdelay)
print("It is a final error given a face. Every failed choice is trapped inside it.")
time.sleep(textdelay)
print("The battle is fought through commands, not luck.")
time.sleep(textdelay)
input("Press enter to face the final boss...")
clear()

def boss_bar(current, maximum):
    percent = max(0, current)
    bars = 20
    filled = int((percent / maximum) * bars)
    return "[" + "#" * filled + "-" * (bars - filled) + "]"

def final_bossfight():
    player_hp = 100
    boss_hp = 150
    charge = 0

    while player_hp > 0 and boss_hp > 0:
        gd.gradient_banner("THE NULL CRAWLER", "#FF0000", "#8B0000")
        print_line()
        print(f"{name}: {boss_bar(player_hp, 100)} {player_hp}/100 HP")
        print(f"NULL CRAWLER: {boss_bar(boss_hp, 150)} {boss_hp}/150 HP")
        print(f"Charge: {charge}/3")
        print_line()

        if charge >= 3:
            print("1. STRIKE - normal attack")
            print("2. GUARD - reduce the boss's next attack")
            print("3. OVERDRIVE - release a devastating charge attack")
        else:
            print("1. STRIKE - normal attack")
            print("2. GUARD - reduce the boss's next attack")
            print("3. CHARGE - gain 1 charge and prepare for overdrive")

        choice = input("Enter a command (1/2/3): ").strip()

        guarding = choice == "2"
        if choice == "1":
            damage = random.randint(12, 19)
            boss_hp -= damage
            print(f"\n{name} strikes the terminal shell for {damage} damage!")
        elif choice == "2":
            print(f"\n{name} raises a guard around the connection.")
        elif choice == "3":
            if charge >= 3:
                damage = random.randint(35, 48)
                boss_hp -= damage
                charge = 0
                print(f"\n{name} releases OVERDRIVE for {damage} damage!")
            else:
                charge += 1
                print(f"\n{name} feeds corrupted code into the command. Charge: {charge}/3")
        else:
            print("\nUnknown command. The boss takes the opening!")

        if boss_hp <= 0:
            break

        time.sleep(textdelayquick)
        if boss_hp <= 50:
            boss_damage = random.randint(17, 25)
            boss_move = "EXECUTE: SYSTEM_CORRUPTION"
        else:
            boss_damage = random.randint(10, 17)
            boss_move = "EXECUTE: DATA_ERASE"

        if guarding:
            reduced = boss_damage - random.randint(8, 12)
            boss_damage = max(3, reduced)
            boss_move += " - BLOCKED"

        player_hp -= boss_damage
        print(f"The NULL CRAWLER uses {boss_move}!")
        print(f"{name} takes {boss_damage} damage.")
        time.sleep(textdelay)

        if player_hp <= 0:
            break
        clear()

    print_line()
    if player_hp <= 0:
        clear()
        gd.gradient_banner("CONNECTION TERMINATED", "#FF0000", "#8B0000")
        print_line()
        print("The terminal closes around you.")
        print(f"The NULL CRAWLER remains, and your run ends at stage {stage}.")
        time.sleep(textdelay)
        endgame()

    clear()
    gd.gradient_banner("NULL CRAWLER DEFEATED", "#D4AF37", "#E0BFB8")
    print_line()
    print("The corruption screen freezes...")
    time.sleep(textdelay)
    print("Then every symbol in the terminal starts returning to normal.")
    time.sleep(textdelay)
    print(f"You survived with {player_hp} HP.")
    print("The final doorway opens, but the crawler's voice follows you out...")
    time.sleep(textdelay)
    gd.gradient_text(f'"There is only one save left, {name}. Yours."', "#D4AF37", "#E0BFB8")
    time.sleep(textdelay)
    gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
    gd.gradient_text("Thanks for playing Terminal Crawler!", "#D4AF37", "#E0BFB8")
    gd.gradient_text("Created by: @butterific", "#D4AF37", "#E0BFB8")

final_bossfight()

