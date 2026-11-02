# import my gradient generator lib
from gradientor import gradient_generators as gd
import time
import os
# clear console function
def clear():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
gd.gradient_banner("Terminal Crawler", "#D4AF37", "#E0BFB8")
gd.gradient_text("-----------------------------------------", "#D4AF37", "#E0BFB8")
gd.gradient_text("A fun, interactive terminal game which progresses through 25 pre generated stages!", "#D4AF37", "#E0BFB8")
# asks for the users name
name = input("To start, Please enter your name: ")
print(f"Hello, {name}! Welcome to Terminal Crawler!")
print("Let's begin!")
time.sleep(3)
clear()
gd.gradient_banner("Stage 1", "#D4AF37", "#E0BFB8")