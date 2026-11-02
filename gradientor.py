import os
import pyfiglet
import random

def clear_console():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def get_gradient(start_hex, end_hex, steps):
    start_rgb = 0
    end_rgb = 0
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    step_r = 0
    step_g = 0
    step_b = 0

    step_r = (end_rgb[0] - start_rgb[0]) / (steps - 1)
    step_g = (end_rgb[1] - start_rgb[1]) / (steps - 1)
    step_b = (end_rgb[2] - start_rgb[2]) / (steps - 1)

    gradient_colors = []
    gradient_colors.clear()
    for i in range(steps):
        r = int(start_rgb[0] + step_r * i)
        g = int(start_rgb[1] + step_g * i)
        b = int(start_rgb[2] + step_b * i)
        gradient_colors.append((r, g, b))

    return gradient_colors
def random_hex_color():
    color = random.randrange(0, 2**24)
    hex_color = hex(color)
    hex_color = hex_color[2:]
    return hex_color
def get_console_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except OSError:
        return 80, 24

class gradient_generators:
    def gradient_banner(text, start_hex, end_hex):
        banner = pyfiglet.figlet_format(text)
        lines = banner.split("\n")

        total_width = max(len(line) for line in lines)
        if total_width == 0:
            return

        gradient = get_gradient(start_hex, end_hex, total_width)

        for line in lines:
            colored_line = ""
            for char_index, char in enumerate(line):
                if char != ' ':
                    if char_index < len(gradient):
                        r, g, b = gradient[char_index]
                        colored_line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
                    else:
                        colored_line += char  
                else:
                    colored_line += ' '
            print(colored_line)
    def gradient_text(text, start_hex, end_hex):
        lines = [text]

        total_width = len(text)
        if total_width == 0:
            return

        gradient = get_gradient(start_hex, end_hex, total_width)
        start_hex = 0
        end_hex = 0
        total_width = 0
        for line in lines:
            colored_line = ""
            for char_index, char in enumerate(line):
                if char != ' ':
                    if char_index < len(gradient):
                        r, g, b = gradient[char_index]
                        colored_line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
                    else:
                        colored_line += char
                else:
                    colored_line += ' '
            print(colored_line)

    def gradient_background(start_hex, end_hex, width, height):
        gradient = get_gradient(start_hex, end_hex, height)

        for r, g, b in gradient:
            colored_line = f"\033[48;2;{r};{g};{b}m{' ' * width}\033[0m"
            print(colored_line)


def render_image(imagepath: str):
    clear_console()
    try:
        with Image.open(imagepath) as img:
            clear_console()
            term_image = AutoImage(img)
            term_image.draw()

    except FileNotFoundError:
        print(f"Error: The file at '{imagepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")