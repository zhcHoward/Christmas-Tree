#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys
import time

last_layer = None
total_lines = 3
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
    """
    Print a christmas tree of the given height.
    """
    for layer in range(layers):
        generate_layer(layer)

    print_tree()


def generate_layer(layer):
    global last_layer, total_lines
    if not last_layer:
        start = 1
        level = 3
    else:
        start = last_layer[0] - 2
        level = last_layer[1] + 1

    cnt = start
    for _ in range(level):
        line = ""
        for _ in range(cnt):
            colored = random.random() < COLOR_POS
            if colored:
                color = random.choice(COLORS)
                line += color + "O" + CEND
            else:
                line += "*"
        tree.append((line, cnt))
        cnt += 2

    last_layer = (cnt - 2, level)
    total_lines += level


def print_tree():
    global init, total_lines
    max_width = last_layer[0]
    content = ""
    for ln, t in enumerate(tree):
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
        last_layer = None
        tree = []
        time.sleep(1)
        total_lines = 3
