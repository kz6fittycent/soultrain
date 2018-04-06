#!/usr/bin/env python3

from os import path
import random
import textwrap
import tkinter as tk

module_data = path.join(path.dirname(__file__), "data")
ascii_path = path.join(module_data, "ascii")

def main():
    with open(ascii_path) as ascii_file:
         print(ascii_file.read))
    
