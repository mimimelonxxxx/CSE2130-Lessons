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

# Example 4: Updating a File 
# Overwrite the contents of the file 
FILE = open(FILENAME, "w")
FILE.write("Dolly the sheep")
FILE = open(FILENAME)
TEXT = FILE.read()
FILE.close() 

# Update contents require the contents to be read first 
TEXT = TEXT.upper() # uppercase all text 
FILE = open(FILENAME, "w")
FILE.write(TEXT)
FILE.close()

# Append content to the end of a file 
FILE = open(FILENAME, "a")
# FILE.write("Sven the reindeer")
FILE.write("\nSven the reindeer") # adds a new line
FILE.close()
FILE = open(FILENAME)
print(FILE.read())
FILE.close()

# Example 3B Reading a file line by line 
FILE = open(FILENAME)
print(FILE.readline())
FILE.close()
FILE = open(FILENAME)
print(FILE.readlines())
FILE.close()
# The method above is not ideal for splittling lines because of the \n symbol

FILE = open(FILENAME)
LINES = FILE.read().splitlines()
FILE.close()
print(LINES)

# Example 5: Deleting a file
import os # need to import the operating system 
os.remove(FILENAME)