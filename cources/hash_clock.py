from datetime import datetime
import os

rules = {
    "1": ("  #", "  #", "  #", "  #", "  #"),
    "2": ("###", "  #", "###", "#  ", "###"),
    "3": ("###", "  #", "###", "  #", "###"),
    "4": ("# #", "# #", "###", "  #", "  #"),
    "5": ("###", "#  ", "###", "  #", "###"),
    "6": ("###", "#  ", "###", "# #", "###"),
    "7": ("###", "  #", "  #", "  #", "  #"),
    "8": ("###", "# #", "###", "# #", "###"),
    "9": ("###", "# #", "###", "  #", "###"),
    "0": ("###", "# #", "# #", "# #", "###"),
    ":": ("   ", " # ", "   ", " # ", "   ")
}


def draw(time):
    os.system("clear")
    for layer in range(5):
        layer_string = ""
        for el in time:
            layer_string += rules[el][layer] + " "
        print(layer_string.rstrip())


if __name__ == '__main__':
    prev_now = ""
    while True:
        now = str(datetime.now())[11:19]
        if now != prev_now:
            draw(now)
            prev_now = now
