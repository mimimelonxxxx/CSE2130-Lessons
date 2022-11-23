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
    # ??? why doesnt this work
    # clean up data
    for i in range(len(TEXTLIST)):
        if TEXTLIST[i][-1] == "\n":
            TEXTLIST[i] = TEXTLIST[:-1] # until the last character
        TEXTLIST[i] = TEXTLIST[i].split(",")
        for j in range(len(TEXTLIST[i])):
            if TEXTLIST[i][j].isnumeric():
                TEXTLIST[i][j] = int(TEXTLIST[i][j])
    return TEXTLIST


def menu() -> int:
    """
    user chooses to search for strengths or weakness
    :return: int
    """
    print("""
Choose an option,
1. Search for a pokemon strength (super effective)
2. Search for a pokemon weakness (not very effective)
3. Exit
    """)
    CHOICE = input("> ")
    return CHOICE

def getPokemonName() -> str:
    """
    user inputs pokemon name
    :return: str
    """
    return input("Pokemon Name: ")

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
        LIST[i][2] = LIST[i][2].lower()
        LIST[i][3] = LIST[i][3].lower()

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

def setupStrongTypes(LIST) -> None:
    """
    load and import pokemon strengths
    :param LIST: list
    :return: None
    """
    global CONNECTION, CURSOR

    for i in range(len(LIST)):
        for j in range(len(LIST[i])):
            if LIST[i][j] == "":
                LIST[i][j] == None

    CURSOR.execute("""
        CREATE TABLE
            strong (
                type TEXT PRIMARY KEY,
                type_1 TEXT,
                type_2 TEXT,
                type_3 TEXT,
                type_4 TEXT,
                type_5 TEXT
            );
    """)

    for i in range(1, len(LIST)):
        CURSOR.execute("""
            INSERT INTO
                strong
            VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
        """, LIST[i])

    CONNECTION.commit()

def getPokemonStrengths(POKEMON):
    """
    queries the database for pokemon type strenghts
    :param POKEMON: str
    :return: list 
    """
    global CURSOR
    TYPE1STRONG = CURSOR.execute("""
        SELECT
            strong.type_1,
            strong.type_2,
            strong.type_3,
            strong.type_4,
            strong.type_5
        FROM
            pokemon
        JOIN
            strong
        ON
            strong.type = pokemon.type_1
        WHERE
            name = ?;
    """, [POKEMON]).fetchone()

    TYPE2STRONG = CURSOR.execute("""
        SELECT 
            strong.type_1,
            strong.type_2,
            type_3,
            type_4,
            type_5
        FROM 
            pokemon
        JOIN
            strong
        ON
            strong.type = pokemon.type_2
        WHERE
            name = ?;
    """, [POKEMON]).fetchone()

    STRENGTHS = []
    for i in range(len(TYPE1STRONG)):
        if TYPE1STRONG[i] is not None:
            STRENGTHS.append(TYPE1STRONG[i])
    if TYPE2STRONG is not None:
        for i in range(len(TYPE2STRONG)):
            if TYPE2STRONG[i] is not None and TYPE2STRONG not in STRENGTHS:
                STRENGTHS.append(TYPE2STRONG[i])
    return STRENGTHS

# OUTPUTS # 

### VARIABLES ###

DATABASEFILE = "pokemon.db"

FIRSTRUN = True 
if (pathlib.Path.cwd() / DATABASEFILE).exists():
    FIRSTRUN = False

CONNECTION = sqlite3.connect(DATABASEFILE)
CURSOR = CONNECTION.cursor()

### MAIN PROGRAM CODE ###
if __name__ == "___main___":
    pass
    # INPUTS # 
    if FIRSTRUN:
        CONTENT = getFileContent("pokemon_no_mega.csv")
        setupPokemon(CONTENT)
        TYPES = getFileContent("pokemon_type_strong.csv")
        setupStrongTypes(TYPES)
    # PROCESSING # 
    CHOICE = menu()
    if CHOICE == 1:
        POKEMON = getPokemonName()
        STRENGTHS = getPokemonStrengths(POKEMON)
    # OUTPUT # 