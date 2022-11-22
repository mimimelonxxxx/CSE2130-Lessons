"""
title: Pokemon Type Checker
author: Michelle Jiang
date-created: 2022-11-21
"""

import pathlib
import sqlite3

### FUNCTIONS ###

# INPUTS # 

def getFileContent(FILENAME) -> list:
    """
    extracts the content of the file into a 2d array
    :param FILENAME: str 
    :return: list 
    """
    FILE = open(FILENAME)
    TEXTLIST = FILE.readlines()
    FILE.close()

    # clean up data

    for i in range(len(TEXTLIST)):
        if TEXTLIST[i][-1] == "\n":
            TEXTLIST[i] = TEXTLIST[:-1] # until the last character
        TEXTLIST[i] = TEXTLIST[i].split(",")
        for j in range(len(TEXTLIST[i])):
            if TEXTLIST[i][j].isnumeric():
                TEXTLIST[i][j] = int(TEXTLIST[i][j])
    return TEXTLIST


# PROCESSING # 

def setupPokemon(LIST) -> None:
    """
    create tables within the database
    :param LIST: list of pokemon
    :return: None
    """
    global CONNECTION, CURSOR

    CURSOR.execute("""
        CREATE TABLE
            pokemon (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            type_1 TEXT NOT NULL,
            type_2 TEXT
            );
    """)

    for i in range(1, len(LIST)):
        CURSOR.execute("""
            INSERT INTO
                pokemon
            VALUES (
                ?, 
                ?,
                ?,
                ?
            );
        """, LIST[i][:4])

    CONNECTION.commit()

# OUTPUTS # 

### VARIABLES ###

DATABASEFILE = "pokemon.db"

if (pathlib.Path.cwd() / DATABASEFILE).exists():
    FIRSTRUN = False
FIRSTRUN = True 

CONNECTION = sqlite3.connect(DATABASEFILE)
CURSOR = CONNECTION.cursor()

### MAIN PROGRAM CODE ###
if __name__ == "___main___":
    pass
    # INPUTS # 
    if FIRSTRUN:
        CONTENT = getFileContent(DATABASEFILE)
        setupPokemon(CONTENT)
    # PROCESSING # 

    # OUTPUT # 