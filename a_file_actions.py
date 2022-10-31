"""
title: Basic File Actions
author: Michelle Jiang 
date-created: 2022-10-31
"""

FILENAME = "a_file.txt"

# Example 1: Create, open and close a file 

try: 
    FILE = open(FILENAME, "x")
    FILE.close() 
except FileExistsError:
    FILE = open(FILENAME)
    FILE.close() 

# Example 2: Write to a file 

FILE = open(FILENAME, "w")
FILE.write("Hello World")
FILE.close()

# Example 3: Read a file 

FILE = open(FILENAME)
TEXT = FILE.read()
TEXT = FILE.readlines()
FILE.close()
print(TEXT)