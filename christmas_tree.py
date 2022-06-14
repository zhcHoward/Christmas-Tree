#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys
import time

from blessed import Terminal

init = True
tree = []
t = Terminal()
COLORS = ("red", "green", "yellow", "blue", "magenta", "cyan")
COLOR_POS = 0.2


def christmas_tree(layers):
    global tree
    tree = []
    for layer in range(layers):
        generate_layer(layer)

    print_tree(layers)


def generate_layer(layer):
    length = layer * layer + layer + 1
    level = layer + 3
    for _ in range(level):
        line = ""
        for _ in range(length):
            colored = random.random() < COLOR_POS
            if colored:
                color = random.choice(COLORS)
                line += getattr(t, color)("O")
            else:
                line += "*"
        tree.append((line, length))
        length += 2


def print_tree(layers):
    layers -= 1
    max_width = tree[-1][1]
    total_lines = len(tree) + 3
    global init
    content = ""
    for leaves, length in tree:
        spaces = (max_width - length) // 2
        content += " " * spaces + leaves + "\n"

    spaces = (max_width - 5) // 2
    for _ in range(2):
        content += " " * spaces + "|   |\n"

    content += " " * spaces + "|___|"
    if init:
        print(content)
        init = False
    else:
        print(t.move_up * total_lines + content)


if __name__ == "__main__":
    layers = int(sys.argv[1])
    try:
        while True:
            christmas_tree(layers)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\rMerry Christmas!")
        sys.exit(0)
