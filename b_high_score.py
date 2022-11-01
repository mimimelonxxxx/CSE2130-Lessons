"""
title: High Score
author: Michelle Jiang
date-created: 2022-11-01
"""

### VARIABLES ### 
FILENAME = "b_score.txt" 

### SUBROUTINES ### 

# INPUTS # 

def getFile(): 
    """
    checks if the save file exists, and creates a default file if it doesnt 
    :return: Object FILE -> read-only 
    """
    global FILENAME 
    try: 
        FILE = open(FILENAME, "x")
        # Create default scores 
        START_SCORE = []
        for i in range(10):
            START_SCORE.append("AAA 0")
        TEXT = ", ".join(START_SCORE)
        FILE.write(TEXT)
        FILE.close()
        # open file as read-only
        FILE = open(FILENAME)
        return FILE 
    except FileExistsError: # always want a parameter for except 
        FILE = open(FILENAME)
        return FILE 

def readFile(FILE_OBJ):
    """
    reads and processes file data into an array
    :param FILE_OBJ: object
    :return: list->str 
    """
    TEXT = FILE_OBJ.read()
    SCORE_ARRAY = TEXT.split(", ")
    return SCORE_ARRAY 

def menu():
    """
    user selects whether to view or add new scores 
    :return: int
    """
    print("""
1. View High Scores 
2. Add High Score
3. Exit 
    """)
    CHOICE = int(input("> "))
    return CHOICE 

def askNewScore():
    """
    asks user for a new score 
    :return: int 
    """
    SCORE = input("What is the new score? ")
    try: 
        SCORE = int(SCORE)
        return SCORE
    except ValueError: 
        print("Enter a valid number! ")
        return askNewScore()

def askName(): 
    """
    user inputs name to be saved
    :return: str
    """
    NAME = input("What is your name? ")
    NAME = NAME.upper()
    if len(NAME) > 3: 
        NAME = NAME[:3]
    return NAME

# PROCESSING # 

def checkNewScore(SCORE, SCORE_LIST):
    """
    compare the new score to all the scores in the array to see if it is higher 
    :param SCORE: int 
    :param SCORE_LIST: list -> str
    :return: boolean
    """
    # Manipulate data in SCORE_LIST 
    SCORE_LIST_2D = []
    for i in range(len(SCORE_LIST)):
        SCORE_LIST_2D.append(SCORE_LIST[i].split())
        SCORE_LIST_2D[-1][1] = int(SCORE_LIST_2D[-1][1]) # gets the number of the last node 
        # Compare SCORE to SCORE_LIST 
        for i in range(len(SCORE_LIST_2D)):
            if SCORE >= SCORE_LIST_2D[i][1]:
                return True
        return False 

# OUTPUTS # 

def viewHighScore(SCORE_LIST):
    """
    displays scores 
    :param SCORE_LIST: list of scores
    :return: None
    """
    for i in range(len(SCORE_LIST)):
        print(f"{i+1}. {SCORE_LIST[i]}")

if __name__ == "__main__": 
        FILER = getFile()
        SCORE_LIST = readFile(FILER)

        while True: 
            CHOICE = menu()
            if CHOICE == 1: 
                viewHighScore(SCORE_LIST)
            elif CHOICE == 2: 
                NEW_SCORE = askNewScore()
                if checkNewScore(NEW_SCORE, SCORE_LIST):
                    NAME = askName()
                    print(NAME)
                else: 
                    print("Better luck next time! ")
            else: 
                exit()