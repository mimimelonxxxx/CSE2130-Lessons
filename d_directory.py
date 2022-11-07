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

def menu() -> int:
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
    return

# OUTPUTS # 

### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    pass
    # INPUTS # 
    if FIRSTRUN: 
        setup()
    CHOICE = menu()
    if CHOICE == 3:
        addContact()
    # PROCESSING # 
    
    # OUTPUTS # 
