#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys
import time

init = True
tree = []

CEND = "\033[0m"
CBLACK = "\033[30m"
CRED = "\033[31m"
CGREEN = "\033[32m"
CYELLOW = "\033[33m"
CBLUE = "\033[34m"
CVIOLET = "\033[35m"
CBEIGE = "\033[36m"
CWHITE = "\033[37m"
CGREY = "\033[90m"
CRED2 = "\033[91m"
CGREEN2 = "\033[92m"
CYELLOW2 = "\033[93m"
CBLUE2 = "\033[94m"
CVIOLET2 = "\033[95m"
CBEIGE2 = "\033[96m"
CWHITE2 = "\033[97m"
COLORS = [
    CRED,
    CGREEN,
    CYELLOW,
    CBLUE,
    CVIOLET,
    CBEIGE,
    CGREY,
    CRED2,
    CGREEN2,
    CYELLOW2,
    CBLUE2,
    CVIOLET2,
    CBEIGE2,
]
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
                line += color + "O" + CEND
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
    for t in tree:
        spaces = (max_width - t[1]) // 2
        content += " " * spaces + t[0] + "\n"

    spaces = (max_width - 5) // 2
    for i in range(2):
        content += " " * spaces + "|   |\n"

    content += " " * spaces + "|___|"
    if init:
        print(content)
        init = False
    else:
        print("\033[F" * total_lines + content)


if __name__ == "__main__":
    layers = int(sys.argv[1])
    while True:
        christmas_tree(layers)
        time.sleep(1)
