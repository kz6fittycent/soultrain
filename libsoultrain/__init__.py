#!/usr/bin/env python3

from os import path
import random
import textwrap

module_data = path.join(path.dirname(__file__), "data")
ascii_path = path.join(module_data, "ascii")
ascii2_path = path.join(module_data, "ascii2")

def main():
    with open(ascii_path) as ascii_file:
         print(ascii_file.read)
         print(ascii_file.closed)
         print(ascii2_file.read)
         print(ascii2_file.closed))
    
    
    
