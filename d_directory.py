"""
title: Contacts Directory
author: Michelle Jiang
date-created: 2022-11-07 
"""

import sqlite3
import pathlib # library for path files 

### VARIABLES ### 

FILENAME = "d_contacts_directory.db"
FIRSTRUN = True

# Test if file name already exists 
if (pathlib.Path.cwd() / FILENAME).exists(): # cwd = current working directory 
    FIRSTRUN = False 

CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

### SUBROUTINES ### 

# INPUTS # 

def menu() -> int: # can use this syntax to check for errors 
    """
    user selects how to interact with the database 
    :return: int 
    """
    print("""
1. Search for a contact 
2. View all contacts 
3. Add contact
4. Edit contact 
5. Delete contact 
6. Exit 
    """)
    CHOICE = int(input("> ")) # needs checks but this is fine for examples
    return CHOICE

def addContact(): 
    """
    user enters a new contact into the database
    :return: None 
    """
    global CURSOR, CONNECTION
    FIRSTNAME = input("First name: ")
    LASTNAME = input("Last name: ")
    EMAIL = input("Email: ")
    INSTA = input("Instagram: ")
    NEWCONTACT = [FIRSTNAME, LASTNAME, EMAIL, INSTA]
    for i in range(len(NEWCONTACT)):
        if NEWCONTACT[i] == "": # checks for blank strings 
            NEWCONTACT[i] = None # replaces them with None so it gives an error 
    # add the contact to database 
    CURSOR.execute("""
        INSERT INTO 
            contacts (
                first_name,
                last_name,
                email,
                instagram
            )
        VALUES (
            ?,
            ?,
            ?,
            ?
        );
    """, NEWCONTACT)

    CONNECTION.commit()

def searchContactName():
    """
    ask for first name of contact
    :return: str
    """
    NAME = input("First Name: ")
    return NAME

# PROCESSING # 

def setup(): 
    """
    creates the database table on first run 
    :return: None
    """
    global CURSOR, CONNECTION # CONNECTION only needs to be globalled when writing to the file, not if it's read-only
    CURSOR.execute("""
    CREATE TABLE 
        contacts ( 
            id INTEGER PRIMARY KEY, 
            first_name TEXT NOT NULL, 
            last_name TEXT, 
            email TEXT NOT NULL, 
            instagram TEXT
        ); 
    """)
    CONNECTION.commit()

def queryContactName(NAME):
    """
    searches the database for the contact
    :param NAME: str
    :return: list(tuples->str)
    """
    global CURSOR

    RESULTS = CURSOR.execute("""
        SELECT 
            first_name,
            last_name, 
            email,
            instagram
        FROM
            contacts
        WHERE
            first_name = ?
        ORDER BY
            first_name,
            last_name;
    """, [NAME]).fetchall() # filtering needs to go before ordering 
    # NAME needs to be in square brackets 
    return RESULTS

# OUTPUTS # 

def displayContacts():
    """
    prints out all contacts 
    :return: None
    """
    global CURSOR
    CONTACTS = CURSOR.execute("""
        SELECT 
            first_name,
            last_name
        FROM
            contacts
        ORDER BY
            first_name,
            last_name;
            """).fetchall() # no one wants to see a list 
            # fetchall() is not in alphabetical order
            # need to use order by to sort 
    print("All Contacts")
    print("===============")
    for CONTACT in CONTACTS:
        print(CONTACT[0], CONTACT[1]) 

def displayResults(RESULTS):
    """
    displays search results
    :param RESULTS: list(tuples->str)
    :return: None
    """
    for CONTACT in RESULTS:
        print(f"{CONTACT[0]} {CONTACT[1]} (email: {CONTACT[2]}) (instagram: {CONTACT[3]})")
### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    pass
    # INPUTS # 
    if FIRSTRUN: 
        setup()
    while True:
        CHOICE = menu()
        # PROCESSING # 
        if CHOICE == 1:
            NAME = searchContactName()
            RESULT = queryContactName(NAME)
            displayResults(RESULT)
        elif CHOICE == 3:
            addContact()
        elif CHOICE == 4:
            pass
        elif CHOICE == 5:
            pass
        elif CHOICE == 6: # better to be more explicit in the code 
            exit()
        # OUTPUTS # 
        elif CHOICE == 2:
            displayContacts()
            # IPO is better for program flow 