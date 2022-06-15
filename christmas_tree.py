#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys
import time

from blessed import Terminal

COLORS = ("red", "green", "yellow", "blue", "magenta", "cyan")
COLOR_POS = 0.2


class ChristmasTree(object):
    def __init__(self, layers=3):
        self.t = Terminal()
        self.tree = []
        self.first_run = True
        self.layers = layers

    def show(self):
        self.gen_tree()
        self.print_tree()

    def gen_tree(self):
        self.tree = []
        for layer in range(self.layers):
            self.gen_layer(layer)

    def gen_layer(self, layer):
        length = layer * layer + layer + 1
        level = layer + 3
        for _ in range(level):
            line = ""
            for _ in range(length):
                colored = random.random() < COLOR_POS
                if colored:
                    color = random.choice(COLORS)
                    line += getattr(self.t, color)("O")
                else:
                    line += "*"
            self.tree.append((line, length))
            length += 2

    def print_tree(self):
        max_width = self.tree[-1][1]
        content = ""
        for leaves, width in self.tree:
            spaces = (max_width - width) // 2
            content += " " * spaces + leaves + "\n"

        spaces = (max_width - 5) // 2
        for _ in range(2):
            content += " " * spaces + "|   |\n"

        content += " " * spaces + "|___|"
        if self.first_run:
            print(content)
            self.first_run = False
        else:
            total_lines = len(self.tree) + 3
            print(self.t.move_up * total_lines + content)


if __name__ == "__main__":
    layers = int(sys.argv[1])
    ct = ChristmasTree(layers)
    try:
        while True:
            ct.show()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\rMerry Christmas!")
        sys.exit(0)
