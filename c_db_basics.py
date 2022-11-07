"""
title: Database Basics
author: Michelle Jiang
date-created: 2022-11-04
"""

import sqlite3

### VARIABLES ### 

FILENAME = "c_contacts.db" # an alternative extension is .sqlite
CONNCETION = sqlite3.connect(FILENAME)
CURSOR = CONNCETION.cursor()

# Create the database table 

CURSOR.execute("""
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY, 
        first_name NOT NULL, 
        email TEXT
    );
""")

CONNCETION.commit() # writes the changes validated in the CURSOR execute into the file. 

# Create rows of data 

CURSOR.execute("""
    INSERT INTO 
        contacts 
    VALUES (
        1, 
        "Michelle", 
        "michellejiang2017@gmail.com"
    );
""") # must write values in order of columns 

# Alternative 

CURSOR.execute("""
    INSERT INTO 
        contacts (
            first_name,
            email
        )
        VALUES (
            "Alice",
            "a.wong@share.epsb.ca"
        );
""") # can insert values into the specified columns 

CONNCETION.commit()

# Read data from the table 

USERS = CURSOR.execute("""
    SELECT
        *
    FROM 
        contacts; 
""").fetchall()

print(USERS)

# make sure you read and check over everything before running or else you will need to delete your database and restart